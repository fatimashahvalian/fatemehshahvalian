import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json

# بارگذاری فایل JSON
with open('/mnt/data/webt1-424911-4d0266d59f02.json', 'r') as f:
    config = json.load(f)

project_id = config.get('project_id')
private_key_id = config.get('private_key_id')
client_email = config.get('client_email')

try:
    df = pd.read_csv('feedback.csv')
except FileNotFoundError:
    df = pd.DataFrame(columns=['Name', 'Email', 'Product Rating', 'Service Rating', 'Comments'])


st.title("User Feedback Survey")

st.write(f"Project ID: {project_id}")
st.write(f"Client Email: {client_email}")

st.header("Please provide your feedback")
name = st.text_input("Name")
email = st.text_input("Email")
product_rating = st.slider("Product Rating", 1, 5)
service_rating = st.slider("Service Rating", 1, 5)
comments = st.text_area("Additional Comments")

if st.button("Submit"):
    new_feedback = {'Name': name, 'Email': email, 'Product Rating': product_rating, 'Service Rating': service_rating, 'Comments': comments}
    df = df.append(new_feedback, ignore_index=True)
    df.to_csv('feedback.csv', index=False)
    st.success("Thank you for your feedback!")

st.header("Feedback Data")
st.dataframe(df)

st.header("Data Analysis")

average_product_rating = df['Product Rating'].mean()
average_service_rating = df['Service Rating'].mean()

st.write(f"Average Product Rating: {average_product_rating:.2f}")
st.write(f"Average Service Rating: {average_service_rating:.2f}")

st.subheader("Product Rating Distribution")
fig, ax = plt.subplots()
df['Product Rating'].value_counts().sort_index().plot(kind='bar', ax=ax)
ax.set_title("Product Rating Distribution")
ax.set_xlabel("Rating")
ax.set_ylabel("Frequency")
st.pyplot(fig)

st.subheader("Service Rating Distribution")
fig, ax = plt.subplots()
df['Service Rating'].value_counts().sort_index().plot(kind='bar', ax=ax)
ax.set_title("Service Rating Distribution")
ax.set_xlabel("Rating")
ax.set_ylabel("Frequency")
st.pyplot(fig)