import openai
import streamlit as st

openai.api_key = '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'

def get_completion(messages, model="gpt-4"):
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,  # Slightly adjusted to allow for more varied responses
    )
    return response.choices[0].message.content

st.title('AI Simulation')

def simulate_education_process():
    # Simulate generating a topic
    topic_messages = [
        {'role': 'system', 'content': 'You are an assistant tasked with generating an engaging and educational topic for a high school lesson.'},
        {'role': 'user', 'content': 'Generate a topic.'},
    ]
    topic = get_completion(topic_messages)
    print("Generated Topic:\n", topic)
    st.success(f"Generated Topic:  \n{topic}")
     
    # Generate context for the topic
    context_messages = [
        {'role': 'system', 'content': 'Provide a detailed context for the following topic, making it understandable and engaging for high school students.'},
        {'role': 'user', 'content': f'Provide context for the topic: {topic}.'},
    ]
    context = get_completion(context_messages)
    print("\nContext:\n", context)
    st.write(f"Generated Context:  \n{context}")

    # Generate a question based on the context
    question_messages = [
        {'role': 'system', 'content': 'Based on the context provided, formulate an insightful question that could stimulate further discussion or research.'},
        {'role': 'user', 'content': f'Generate a question based on the context: {context}.'},
    ]
    question = get_completion(question_messages)
    print("\nQuestion:\n", question)
    st.success(f"Generated Question:  \n{question}")

    # Simulate a student's answer to the question
    answer_messages = [
        {'role': 'system', 'content': 'Now, simulate a thoughtful and comprehensive answer from a student’s perspective to the previously generated question.'},
        {'role': 'user', 'content': f'Answer the question: {question}'},
    ]
    answer = get_completion(answer_messages)
    print("\nStudent's Answer:\n", answer)
    st.write(f"Generated Answer:  \n{answer}")

    # Evaluate the simulated student's answer
    evaluation_messages = [
        {'role': 'system', 'content': 'Evaluate the student’s answer, providing constructive feedback and highlighting areas for improvement or further exploration.'},
        {'role': 'user', 'content': f'Evaluate the answer: {answer}'},
    ]
    evaluation = get_completion(evaluation_messages)
    print("\nEvaluation:\n", evaluation)
    st.success("Generated Evaluation")
    st.write(evaluation)

if __name__ == "__main__":
    simulate_education_process()
