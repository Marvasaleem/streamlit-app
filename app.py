import streamlit as st
st.title("Streamlit Demo app")

st.header("Heading of streamlit")

st.subheader("Sub-Heading of streamlit")

st.text("This is a text")

st.success("Success")

st.warning("warning")

st.info("information")

st.error("Error")

if st.checkbox("select/Unselect"):
    st.text("user selected the checkbox")
else:
    st.text("user has not selected the checkbox")

state = st.radio("what is your favourite color?", ("Red", "Green", "Yellow"))

if state == 'Green':
    st.success("Thats my favourite color as well")

occupation = st.selectbox("What do you do ?",
["Student","Vlogger","Engineer"])

st.text(f"selected option is {occupation}")

if st.button("Example Button"):
    st.error("you clicked it")

st.sidebar.header("Heading of sidebar")
st.sidebar.text("created by marva")