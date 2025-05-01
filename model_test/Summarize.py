import pandas as pd
import json
from google import genai

def summarize_reviews(reviews_df):

    """
    Summarize the most recent 20 reviews from a dataframe.
    
    Args:
        reviews_df (pandas.DataFrame): DataFrame containing reviews
        
    Returns:
        pandas.DataFrame: DataFrame containing the 20 most recent reviews
    """
    # Make a copy to avoid modifying the original dataframe
    df = reviews_df.copy()
    
    # Ensure the 'date' column is in datetime format if it exists
    if 'date' in df.columns:
        # Convert to datetime if not already
        if not pd.api.types.is_datetime64_any_dtype(df['date']):
            df['date'] = pd.to_datetime(df['date'], errors='coerce')
        
        # Sort by date in descending order (most recent first)
        df = df.sort_values(by='date', ascending=False)
    
    # Take the top 20 rows
    recent_reviews = df.head(40)
    # Fix the regex pattern in the f-string to avoid backslash in expression
    reviews_text = recent_reviews['comment'].str.strip().str.replace(r'\n+', ' ', regex=True).to_string(index=False)
    prompt = f'''
    You are an AI assistant tasked with summarizing student reviews for a professor. Below are {len(recent_reviews)} reviews from students.
    
    Please analyze these reviews and provide:
    
    Summary: A concise summary (3-4 sentences) of the overall sentiment toward this professor
    Teaching Style: The professor's apparent teaching style based on student comments
    Strengths: The main strengths mentioned by students
    Weaknesses: The main weaknesses or criticisms mentioned by students
    Advice: Any consistent advice students give to future classmates about this professor
    
    Reviews:
    {reviews_text}
    
    Please be objective and balanced in your summary, reflecting both positive and negative feedback if present.
    Include no greeting or starting message, simply respond with ONLY the summary.
    '''
    
    return query_gemini(prompt)

def query_gemini(prompt):
    # Load environment variables from .json file
    with open(".env.json") as f:
        env_vars = json.load(f)

    # Get the Google API key from environment variables
    GOOGLE_API_KEY = env_vars['GOOGLE_API_KEY']

    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY not found in environment variables. Please check your .env.json file.")

    client = genai.Client(api_key=GOOGLE_API_KEY)
    #Real version uses a config for a desired content, we will just go with a more simple version here
    return client.models.generate_content(
        model='gemini-2.0-flash',
        contents=prompt
    ).text