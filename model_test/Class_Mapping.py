def get_mapping_for_professor(reviews, verbose=0):
    # Extract only needed columns and filter out non-string class values early
    reviews = reviews[['pid', 'class']]
    reviews = reviews[reviews['class'].apply(lambda x: isinstance(x, str))]
    
    if reviews.empty:
        return None, False
    
    # Check if all professor IDs are the same
    first_pid = reviews['pid'].iloc[0]
    all_same_pid = (reviews['pid'] == first_pid).all()
    
    if not all_same_pid:
        if verbose:
            print(f"Warning: Not all reviews have the same professor ID. Found {reviews['pid'].nunique()} unique professor IDs.")
        return None, False
    
    # Get class list once and pass over the class list once
    class_list = reviews['class'].dropna().tolist()
    total_classes = len(class_list)
    # If no classes, return early
    if total_classes == 0:
        if verbose:
            print("No classes found.")
        return {'misc': {'list': class_list}}, False
    
    unique_classes = reviews['class'].unique()
    counts = {}
    for class_name in class_list:
        digits = len(''.join(filter(str.isdigit, class_name)))
        counts[digits] = counts.get(digits, 0) + 1
    
    # Check for majority digit count
    majority_threshold = 0.6
    majority_digit_count = None
    
    for digits, count in counts.items():
        percentage = count / total_classes
        if percentage > majority_threshold:
            majority_digit_count = digits
            if verbose:
                print(f"Found a majority digit count: {digits} digits (appears in {count}/{total_classes} classes, {percentage:.2%})")
            break
    
    # If no clear majority, determine best approach
    if majority_digit_count is None:
        if verbose:
            print(f"No majority digit count found. Distribution: {counts}")
        
        # Count class occurrences, now for overall reviews
        class_counts = {}
        for class_name in class_list:
            class_counts[class_name] = class_counts.get(class_name, 0) + 1
        
        # Find classes with >10% occurrence in overall reviews
        threshold = 0.1 * total_classes
        significant_classes = {cls: count for cls, count in class_counts.items() if count >= threshold}
        
        if significant_classes:
            if verbose:
                print(f"Found {len(significant_classes)} classes with >10% of reviews")
            
            # Create class mapping with significant classes and misc
            class_mapping = {}
            for cls in significant_classes:
                class_mapping[cls] = {'list': [cls]}
            
            # Add all other classes to misc
            misc_classes = [cls for cls in class_list if cls not in significant_classes]
            class_mapping['misc'] = {'list': misc_classes}
            
            return class_mapping, True
        else:
            if verbose:
                print("No classes with >10% of reviews found, using most common digit count")
            
            # Determine digit count to use
            majority_digit_count = 3 if counts.get(3, 0) > 0 else max(counts.items(), key=lambda x: x[1])[0] if counts else None
    
    # Initialize class mapping
    class_mapping = {'misc': {'list': []}}
    
    # Special handling for zero-digit case
    if majority_digit_count == 0:
        # Count class occurrences for threshold calculation
        class_counts = {}
        for class_name in class_list:
            class_counts[class_name] = class_counts.get(class_name, 0) + 1
        
        # Find classes with >10% occurrence
        threshold = 0.1 * total_classes
        significant_classes = {cls: count for cls, count in class_counts.items() if count >= threshold}
        
        # Extract alpha-only versions of class names
        alpha_only_classes = {}
        for class_name in unique_classes:
            alpha_only = ''.join(filter(str.isalpha, class_name.upper()))
            if alpha_only:
                alpha_only_classes[class_name] = alpha_only
            else:
                class_mapping['misc']['list'].append(class_name)
        
        # Group classes by substring containment
        grouped = {}
        ungrouped = set(alpha_only_classes.keys())
        
        # Sort by length descending to prioritize longer strings as group labels
        sorted_classes = sorted(alpha_only_classes.keys(), key=lambda x: len(alpha_only_classes[x]), reverse=True)
        
        for potential_group in sorted_classes:
            if potential_group not in ungrouped:
                continue
                
            alpha_potential = alpha_only_classes[potential_group]
            group_members = [potential_group]
            ungrouped.remove(potential_group)
            
            # Find all classes that are substrings (in order) of this one
            for other_class in list(ungrouped):
                alpha_other = alpha_only_classes[other_class]
                
                # Check if letters from other_class appear in the same order in potential_group
                i, j = 0, 0
                while i < len(alpha_other) and j < len(alpha_potential):
                    if alpha_other[i] == alpha_potential[j]:
                        i += 1
                    j += 1
                
                if i == len(alpha_other):  # All letters found in order
                    group_members.append(other_class)
                    ungrouped.remove(other_class)
            
            # Use the class name as key if it has >10% reviews, otherwise use the alpha string
            group_key = potential_group
            if not any(cls in significant_classes for cls in group_members):
                if len(group_members) == 1:
                    class_mapping['misc']['list'].extend(group_members)
                    continue
                
            grouped[group_key] = group_members
        
        # Add grouped classes to mapping
        for group_key, group_members in grouped.items():
            class_mapping[group_key] = {'list': group_members, 'prefix': '', 'suffix': ''}

        return class_mapping, True #no need to do prefix or suffix as only strings
    else:
        # Process classes with digits
        for class_name in unique_classes:
            strnumbers = ''.join(filter(str.isdigit, class_name))
            
            if not strnumbers:
                class_mapping['misc']['list'].append(class_name)
                continue
            
            try:
                number = int(strnumbers)
                digits = len(strnumbers)
                
                if majority_digit_count is not None:
                    if digits == majority_digit_count:
                        if number not in class_mapping:
                            class_mapping[number] = {'list': []}
                        class_mapping[number]['list'].append(class_name)
                    elif digits > majority_digit_count and majority_digit_count != 0 and digits % majority_digit_count == 0:
                        # Split the number into sections
                        for i in range(0, len(strnumbers), majority_digit_count):
                            section_num = int(strnumbers[i:i+majority_digit_count])
                            if section_num not in class_mapping:
                                class_mapping[section_num] = {'list': []}
                            class_mapping[section_num]['list'].append(class_name)
                    else:
                        class_mapping['misc']['list'].append(class_name)
                else:
                    class_mapping['misc']['list'].append(class_name)
            except ValueError:
                class_mapping['misc']['list'].append(class_name)

    # Find common prefixes and suffixes
    from itertools import takewhile
    from collections import Counter
    
    for class_number in list(class_mapping.keys()):
        if class_number == 'misc':
            continue
            
        class_list = class_mapping[class_number]['list']
        
        # Extract prefixes and suffixes in one pass
        prefixes = []
        suffixes = []
        
        for class_name in class_list:
            prefix = ''.join(takewhile(lambda x: not x.isdigit(), class_name))
            suffix = ''.join(takewhile(lambda x: not x.isdigit(), class_name[::-1]))[::-1]
            
            prefixes.append(prefix)
            suffixes.append(suffix)
        
        # Use Counter for efficient counting
        prefix_counter = Counter(prefixes)
        suffix_counter = Counter(suffixes)
        
        # Get most common prefix and suffix
        class_mapping[class_number]['prefix'] = prefix_counter.most_common(1)[0][0] if prefix_counter else ""
        class_mapping[class_number]['suffix'] = suffix_counter.most_common(1)[0][0] if suffix_counter else ""
    
    return class_mapping, majority_digit_count is not None

def get_median_grade_by_class(reviews, class_mapping):
    import pandas as pd
    
    # Unpack the tuple if class_mapping is a tuple
    if isinstance(class_mapping, tuple):
        class_mapping = class_mapping[0]
    
    result = {}
    
    for class_num in class_mapping:
        if class_num == 'misc':
            continue
            
        class_list = class_mapping[class_num]['list']
        grades = reviews[reviews['class'].isin(class_list)][['grade']].dropna()
        
        # Define the order of grades for categorical ranking
        grade_order = ['F', 'D-', 'D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+']
        
        # Filter out non-standard grades
        valid_grades = grades[grades['grade'].isin(grade_order)].copy()
        
        if valid_grades.empty:
            result[class_num] = None
            continue
        
        # Convert grades to categorical type with defined order
        valid_grades.loc[:, 'grade_cat'] = pd.Categorical(
            valid_grades['grade'], 
            categories=grade_order, 
            ordered=True
        )
        
        # Sort and select the middle value
        sorted_grades = valid_grades.sort_values('grade_cat')
        middle_idx = len(sorted_grades) // 2
        result[class_num] = sorted_grades.iloc[middle_idx]['grade']
    
    return result