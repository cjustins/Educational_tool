import streamlit as st
import openai


openai.api_key = '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'

def get_completion(messages, model="gpt-4"):
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content

# Streamlit app layout
st.title('AI-driven Education Tool')

# Input for the topic
topic = st.text_input("Enter a topic:", "")

if topic:
    # Generate context on the topic
    context_prompt = f"Provide a context for the topic: {topic}."
    messages_topic =  [  
{'role':'system', 
 'content':"""You are an assistant who will generate a context for the topic that a student fills in.
 Try to understand the meaning of the provided topic
 Identify the field of study that the topic relates to
 Suggest meaningful information that can be provided in the context
 Provide a context about that particular topic"""},    
{'role':'user', 
 'content':f"{context_prompt}"},  
] 
    context = get_completion(messages_topic)
    st.text_area("Context:", value=context, height=300, disabled=True)

    # Generate a question 
    system_message = f"""
Follow these steps to generate a question that will be answered by the student.

Step 1:Identify possible questions that can be asked in the particular context. 

Step 2:Try to make sure that your question lies within the domain of the context. 

Step 3:Ask a question that you can evaluate
"""
    
    question_prompt = f"Based on the context: {context}, generate an open-ended question that a student should answer."
    messages_question =  [  
{'role':'system', 
 'content': system_message},    
{'role':'user', 
 'content':f"{question_prompt}"},  
] 
    question = get_completion(messages_question)
    st.text_area("Question:", value=question, height=100, disabled=True)

    # Input for the student's answer
    answer = st.text_area("Your Answer:")

    if st.button('Submit Answer'):
        # Assess the answer 
        assessment_prompt = f"Assess this answer to the question '{question}': {answer}"
        messages_assess = [  
{'role':'system', 
 'content':"""You are required to assess the answer provided by the student"""},    
{'role':'user', 
 'content':f"{assessment_prompt}"},  
] 
        feedback = get_completion(messages_assess)
        st.text_area("Feedback:", value=feedback, height=200, disabled=True)
