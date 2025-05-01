from Categorical import get_rating_tags_distribution

def get_mean_difficulty(df):
    return float(df['difficultyRating'].mean())

def get_mean_quality(df):
    return float(df['qualityRating'].mean())

def get_would_take_again_percentage(df):
    df = df.dropna(subset=['wouldTakeAgain'])
    return float(df['wouldTakeAgain'].mean())

def get_attendance_mandatory_percentage(df):
    df = df.dropna(subset=['attendanceMandatory'])
    df['attendanceMandatory'] = df['attendanceMandatory'].map({'mandatory': 1, 'non mandatory': 0, 'Y': 1, 'N': 0})
    df = df[df['attendanceMandatory'].isin([0,1])]
    return float(df['attendanceMandatory'].mean())

def get_top_tags(df):
    tags = get_rating_tags_distribution(df)
    # Convert tuples to lists for JSON serialization
    return [list(x) for x in sorted(tags.items(), key=lambda x: x[1], reverse=True)[:5]]

def get_comment_length(df):
    return float(df['comment'].apply(len).mean())

def get_is_online_percentage(df):
    df = df.dropna(subset=['isForOnlineClass'])
    df['isForOnlineClass'] = df['isForOnlineClass'].map({True: 1, False: 0})
    return float(df['isForOnlineClass'].mean())

def get_is_for_credit_percentage(df):
    df = df.dropna(subset=['isForCredit'])
    df['isForCredit'] = df['isForCredit'].map({True: 1, False: 0})
    return float(df['isForCredit'].mean())

def get_tag_score(Overall_tags):
    tags = { # Arbitrary decision of how 'good' and 'bad' tags are, in descending order
        # Positive tags (> 0.6)
        'amazing_lectures': 0.90,
        'extra_credit': 0.85,
        'gives_good_feedback': 0.85,
        'caring': 0.80,
        'inspirational': 0.75,
        'respected': 0.75,
        'accessible_outside_class': 0.70,
        'hilarious': 0.70,
        'online_savvy': 0.65,
        
        # Neutral tags (0.4 - 0.6)
        'clear_grading_criteria': 0.60,
        'participation_matters': 0.55,
        'lecture_heavy': 0.50,
        'group_projects': 0.50,
        'test_heavy': 0.40,
        
        # Negative tags (< 0.4)
        'graded_by_few_things': 0.4,
        'get_ready_to_read': 0.30,
        'tough_grader': 0.25,
        'lots_of_homework': 0.20,
        'so_many_papers': 0.15,
        'beware_of_pop_quizzes': 0.10
    }

    score = 0
    for tag in tags:
        if tag in Overall_tags:
            score += Overall_tags[tag] * tags[tag]
    score = score / sum(Overall_tags.values())
    return score
