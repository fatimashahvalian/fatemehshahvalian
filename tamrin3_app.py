import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ایجاد یا بارگذاری دیتافریم برای ذخیره داده‌ها
try:
    df = pd.read_csv('feedback.csv')
except FileNotFoundError:
    df = pd.DataFrame(columns=['Name', 'Email', 'Product Rating', 'Service Rating', 'Comments'])

# عنوان برنامه
st.title("User Feedback Survey")

# فرم نظرسنجی
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

# نمایش داده‌های جمع‌آوری‌شده
st.header("Feedback Data")
st.dataframe(df)

# تحلیل و نمایش نمودار
st.header("Data Analysis")

# میانگین امتیازات
average_product_rating = df['Product Rating'].mean()
average_service_rating = df['Service Rating'].mean()

st.write(f"Average Product Rating: {average_product_rating:.2f}")
st.write(f"Average Service Rating: {average_service_rating:.2f}")

# نمودار امتیازات محصول
st.subheader("Product Rating Distribution")
fig, ax = plt.subplots()
df['Product Rating'].value_counts().sort_index().plot(kind='bar', ax=ax)
ax.set_title("Product Rating Distribution")
ax.set_xlabel("Rating")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# نمودار امتیازات خدمات
st.subheader("Service Rating Distribution")
fig, ax = plt.subplots()
df['Service Rating'].value_counts().sort_index().plot(kind='bar', ax=ax)
ax.set_title("Service Rating Distribution")
ax.set_xlabel("Rating")
ax.set_ylabel("Frequency")
st.pyplot(fig)