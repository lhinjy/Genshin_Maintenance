import streamlit as st
import data_utils

def display_user_input():
    col1, col2= st.columns(2)
    with col1:
        COUNTRY_LIST = data_utils.get_country_names()
        country_chosen = st.multiselect("Type/Select Country Name",COUNTRY_LIST)
        country_button = st.button("Search", key="country")
    with col2:
        UTC_TIMEZONE_LIST = data_utils.get_utc_timezones()
        utc_timezone_chosen = st.selectbox("Select UTC Time Offset",UTC_TIMEZONE_LIST)
        utc_timezone_button = st.button("Search", key ="utc")

    return country_chosen,country_button, utc_timezone_chosen, utc_timezone_button

def write_custom_header(text):
    st.markdown("""
    <style>
    .header-font {
        font-size: 11vw !important;
    }
    .centeralize-content {
        display:flex;
        flex-direction: row;
        justify-content: center;
        width:100vw;
        margin-left: calc(-50vw + 50%);
    }

    </style>
    """, unsafe_allow_html=True)
    

    st.markdown(f'<div class="header-font centeralize-content">{text}</div>', unsafe_allow_html=True)

def write_custom_text(text):
    st.markdown("""
    <style>
    .text-font {
        font-size:2vw !important;
    }

    .centeralize-content {
        display : flex;
        flex-direction: row;
        justify-content: center;
        width:100vw;
        margin-left: calc(-50vw + 50%);
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown(f'<p class="text-font centeralize-content">{text}</p>', unsafe_allow_html=True)

def write_disclaimer():
    st.markdown("""
        <style>
        .custom_footer {
            position: absolute;
            bottom: 10px;
            right: 16px;
            font-size: 12px;
        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown(f'<p class="custom_footer">This is not an official tool by MiHoYo. Source code is available on <a href ="https://github.com/lhinjy/Genshin_Maintenance">github</a></p>', unsafe_allow_html=True)


def main():
    write_disclaimer()

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

    write_custom_header(formatted_datemonth)
    write_custom_header(formatted_time)

main()