import data_utils
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="GI Maintenance",page_icon="🌻", layout="wide")
def display_user_input():
    col1, col2= st.columns(2)
    with col1:
        COUNTRY_LIST = data_utils.get_country_names()
        country_chosen = st.multiselect("Type/Select City Name",COUNTRY_LIST)
        country_button = st.button("Search", key="country")
        with st.expander("See example searches"):
            write_custom_small_text("*Search for your nearest city (not country)")
            write_custom_small_text("Tokyo &#x2705 Japan &#9940 ")
            write_custom_small_text("Beirut &#x2705 Lebanon &#9940")
            write_custom_small_text("Berlin &#x2705 Germany &#9940")
            write_custom_small_text("Stockholm &#x2705 Sweden &#9940")
            write_disclaimer("... you get the idea!")

    with col2:
        UTC_TIMEZONE_LIST = data_utils.get_utc_timezones()
        utc_timezone_chosen = st.selectbox("Select UTC Time Offset",UTC_TIMEZONE_LIST)
        utc_timezone_button = st.button("Search", key ="utc")

    return country_chosen,country_button, utc_timezone_chosen, utc_timezone_button

def write_custom_header(text):
    st.markdown("""
    <style>
    .header-font {
        font-size: 9vw !important;
    }
    .header-container {
        display:flex;
        flex-direction: row;
        justify-content: center;
        width:100vw;
        margin-left: calc(-50vw + 50%);
    }

    </style>
    """, unsafe_allow_html=True)
    

    st.markdown(f'<div class="header-font header-container">{text}</div>', unsafe_allow_html=True)

def write_custom_text(text):
    st.markdown("""
    <style>
    .text-font {
        font-size:3vw !important;
    }

    .text_container {
        display : flex;
        flex-direction: row;
        justify-content: center;
        width:100vw;
        margin-left: calc(-50vw + 50%);
        margin-top:-50px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown(f'<p class="text-font text_container">{text}</p>', unsafe_allow_html=True)

def write_custom_small_text(text):
    st.markdown("""
    <style>
    .small_font {
        font-size: 12px;
        margin-bottom:0px;
        margin-top:-10px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown(f'<p class="small_font">{text}</p>', unsafe_allow_html=True)

def write_disclaimer(text):
    st.markdown("""
        <style>
        .bottom_right {
            position: absolute;
            bottom: 10px;
            right: 16px;
            font-size: 12px;
            margin-top:0px;
            margin-bottom:0px;
        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown(f'<p class="bottom_right">{text}</p>', unsafe_allow_html=True)

def custom_footer():
    footer="""
        <style>
            a:link , a:visited{
            color: #2B3034;
            background-color: transparent;
            }

            a:hover,  a:active {
            color: #d48585;
            background-color: transparent;
            }

            .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100vw;
            background-color: #FCFBF9;
            color: #2B3034;
            text-align: center;
            }
        </style>
        <div class="footer">
            <i class="fas fa-heart"></i>
            <p>Developed with  <a href="https://github.com/lhinjy"  target="_blank"> ❤ </a> by a frustrated Genshin player</p>
            <p> <a href="https://github.com/lhinjy/Genshin_Maintenance"  target="_blank">GitHub</a> || <a href="https://ko-fi.com/lhinjy"  target="_blank">Ko-fi</a></p>
        </div>
        """
    st.markdown(footer,unsafe_allow_html=True)


def main():
    # st.write("This is not an official tool by MiHoYo. Source code is available on my [Github](https://github.com/lhinjy/Genshin_Maintenance)")
    write_disclaimer("This is not an official tool by MiHoYo.")
    write_custom_text("Genshin Impact 2.2 Maintenance Starts At:")
    country_chosen,country_button, utc_timezone_chosen, utc_timezone_button = display_user_input()
    
    formatted_datemonth = ""
    formatted_time = ""
    if country_button:
        try:
            local_maintenance_datetime = data_utils.get_time_information_by_country_name(country_chosen[0])
            formatted_datemonth, formatted_time = data_utils.date_time_formatter(local_maintenance_datetime)
        except:
            pass

    if utc_timezone_button:
        try:
            local_maintenance_datetime = data_utils.get_time_information_by_UTC_offset(utc_timezone_chosen)
            formatted_datemonth, formatted_time = data_utils.date_time_formatter(local_maintenance_datetime)
        except:
            pass
    st.markdown("""<hr style="height:2px;border:none;background-color:#FCFBF9;margin-top:-10px;" /> """, unsafe_allow_html=True)

    write_disclaimer("Time format is in 24-Hour")
    write_custom_header(formatted_datemonth)
    write_custom_header(formatted_time)
    custom_footer()

main()