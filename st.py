import streamlit as st
import requests
from bs4 import BeautifulSoup


st.markdown("""

[بازگشت به وب سایت آکادکی یک] (https://yek.academy)

""")

def fetch_html(url):
    response = requests.get(url)
    return response.text

def main():
    st.title("بررسی سئو داخلی سایت")

    url = st.text_input("آدرس سایت را وارد کنید:")
    keyword = st.text_input("کلمه کلیدی این صفحه را وارد کنید:")

    if url and keyword:
        html = fetch_html(url)
        soup = BeautifulSoup(html,'html.parser')

        # بررسی عنوان
        title_tag = soup.title.string if soup.title else ''
        title_len = len(title_tag)
        st.subheader("عنوان ")
        st.write("عنوان:" , title_tag)
        st.write("طول عنوان:" , title_len)
        if 50 <= title_len <= 60:
         st.success("طول عنوان عالیه")
        else:
          st.warning("طول عنوان مناسب نمی باشد")
        if keyword.lower() in title_tag.lower():
         st.success("کلمه کلیدی در عنوان وجود دارد")
        else:
         st.warning("کلمه کلیدی در عنوان وجود ندارد")
         st.warning("بهتره که از کلمه کلیدی در عنوان استفاده کنی")

         # بررسی متادیسکریپشن
        desc_tag = soup.find("meta", attrs={"name": "description"})
        meta_desc = desc_tag["content"] if desc_tag and "content" in desc_tag.attrs else ''
        meta_len = len(meta_desc)
        st.subheader("متادیسکرپیشن: ")
        st.write("متادیسکرپیشن: " , meta_desc)
        st.write("طول متادیسکرپیشن: " , meta_len)
        if 120 <= meta_len <= 160:
            st.success("طول متا عالیه")
        else:
            st.warning("طول متا مناسب نمی باشد")
        if keyword.lower() in meta_desc.lower():
            st.success("کلمه کلیدی در متادیسکرپیشن وجود دارد")
        else:
            st.warning("کلمه کلیدی در متادیسکپریشن وجود ندارد")

        # بررسی H1
        h1_tag = soup.find("h1")
        st.subheader("H1")
        if h1_tag is not None:
         st.success("کارت درسته. تو صفحه یدونه اچ 1 داری")
        else:
            st.warning("تعداد اچ 1 های این صفحه یا 0 یا بیشتر از 1 می باشد")

        # شمارش کلمات صففحه
        text = soup.get_text()
        word_count = len(text.split())
        st.subheader("بررسی تعداد کلمات این صفحه")
        st.write("تعداد کلمات این صفحه:" ,word_count)
        if word_count >= 350:
            st.success("تعداد کلماتت اوکی هست")
        else:
            st.warning("تعداد کلمات صفحه بهتره که از 350 تا بیشتر باشه")


if __name__ == "__main__":
    main()

