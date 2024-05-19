import streamlit as st
import random
from datetime import datetime
import pandas as pd
import calendar
import time

# Define airline-themed colors
primary_color = '#0066cc'  # Blue
secondary_color = '#ffcc00'  # Yellow
text_color = '#333333'  # Dark Gray
background_color = '#f0f0f5'  # Light Gray

# Define flight details
flight_details = [
    {"Flight No": "AI101", "Departure": "Mumbai", "Destination": "Delhi", "Departure Time": "06:00 AM",
     "Arrival Time": "08:00 AM", "Gate": "A1", "Status": "On Time"},
    {"Flight No": "AI102", "Departure": "Delhi", "Destination": "Mumbai", "Departure Time": "09:00 AM",
     "Arrival Time": "11:00 AM", "Gate": "A2", "Status": "Delayed"},
    {"Flight No": "AI103", "Departure": "Bangalore", "Destination": "Chennai", "Departure Time": "12:00 PM",
     "Arrival Time": "01:30 PM", "Gate": "B1", "Status": "On Time"},
    {"Flight No": "AI104", "Departure": "Chennai", "Destination": "Bangalore", "Departure Time": "02:00 PM",
     "Arrival Time": "03:30 PM", "Gate": "B2", "Status": "On Time"},
    {"Flight No": "AI105", "Departure": "Kolkata", "Destination": "Hyderabad", "Departure Time": "04:00 PM",
     "Arrival Time": "06:00 PM", "Gate": "C1", "Status": "Delayed"},
    {"Flight No": "AI106", "Departure": "Hyderabad", "Destination": "Kolkata", "Departure Time": "07:00 PM",
     "Arrival Time": "09:00 PM", "Gate": "C2", "Status": "On Time"},
    {"Flight No": "AI107", "Departure": "Mumbai", "Destination": "Bangalore", "Departure Time": "10:00 PM",
     "Arrival Time": "12:00 AM", "Gate": "D1", "Status": "On Time"},
    {"Flight No": "AI108", "Departure": "Bangalore", "Destination": "Mumbai", "Departure Time": "01:00 AM",
     "Arrival Time": "03:00 AM", "Gate": "D2", "Status": "On Time"},
    {"Flight No": "AI109", "Departure": "Delhi", "Destination": "Chennai", "Departure Time": "04:00 AM",
     "Arrival Time": "06:00 AM", "Gate": "E1", "Status": "On Time"},
    {"Flight No": "AI110", "Departure": "Chennai", "Destination": "Delhi", "Departure Time": "07:00 AM",
     "Arrival Time": "09:00 AM", "Gate": "E2", "Status": "Delayed"},
]

# Define motivational quotes
motivational_quotes = [
    "The sky is not the limit, it’s just the beginning.",
    "Travel far, travel wide, travel often.",
    "Your wings already exist. All you have to do is fly.",
    "The world is a book, and those who do not travel read only a page.",
    "Adventure awaits, go find it.",
    "The journey of a thousand miles begins with one step.",
]

# Function to generate recommendations based on user input
def generate_recommendations(customer_type, problem_domains):
    # Define recommendation options based on customer type and problem domains
    recommendation_options = {
        ("Loyal Customer", "Seat Comfort"): [
            "Consider upgrading to a premium economy seat for extra comfort on long flights.",
            "Book a seat with extra legroom for added comfort during your flight.",
            "Upgrade to business class for a more luxurious travel experience.",
        ],
        ("Loyal Customer", "Inflight Entertainment"): [
            "Explore our extensive selection of movies, TV shows, and music available on board.",
            "Upgrade to a premium cabin for access to exclusive entertainment options.",
            "Download our mobile app to enjoy in-flight entertainment on your personal device.",
        ],
        ("Loyal Customer", "Food and Drink"): [
            "Pre-order a special meal for your dietary preferences or restrictions.",
            "Try our premium meal options for a gourmet dining experience in the air.",
            "Book a flight during meal service times to enjoy complimentary snacks and beverages.",
        ],
        ("Non-Frequent Customer", "Seat Comfort"): [
            "Consider upgrading to a premium economy seat for extra comfort on long flights.",
            "Book a seat with extra legroom for added comfort during your flight.",
            "Upgrade to business class for a more luxurious travel experience.",
        ],
        ("Non-Frequent Customer", "Inflight Entertainment"): [
            "Explore our extensive selection of movies, TV shows, and music available on board.",
            "Upgrade to a premium cabin for access to exclusive entertainment options.",
            "Download our mobile app to enjoy in-flight entertainment on your personal device.",
        ],
        ("Non-Frequent Customer", "Food and Drink"): [
            "Pre-order a special meal for your dietary preferences or restrictions.",
            "Try our premium meal options for a gourmet dining experience in the air.",
            "Book a flight during meal service times to enjoy complimentary snacks and beverages.",
        ],
        ("Loyal Customer", "On-time Performance"): [
            "Check-in online to save time at the airport and avoid long queues.",
            "Subscribe to flight status notifications for real-time updates on any delays or changes.",
            "Choose flights with longer layovers to reduce the risk of missing connecting flights.",
        ],
        ("Loyal Customer", "Baggage Handling"): [
            "Attach a durable luggage tag with your contact information to easily identify your baggage.",
            "Consider purchasing travel insurance to cover any lost or damaged luggage.",
            "Pack essential items in your carry-on bag in case your checked luggage is delayed or lost.",
        ],
        ("Loyal Customer", "Online Booking"): [
            "Join our loyalty program for exclusive access to special deals and discounts.",
            "Use our mobile app or website for a seamless online booking experience.",
            "Subscribe to our newsletter for updates on promotions and new routes.",
        ],
    }

    # Get recommendations based on user input
    recommendations = {domain: recommendation_options.get((customer_type, domain), []) for domain in problem_domains}

    return recommendations

# Function to display the dashboard
def show_dashboard():
    # Display user profile information
    st.sidebar.title("User Profile")
    st.sidebar.image("Flightops1.png", use_column_width=True)
    position = st.sidebar.selectbox("Select Your Position:", ["FlightOps Manager", "Customer Service Representative", "Pilot", "Cabin Crew"])

    # Display flight details table with enhanced styling
    st.subheader("Next Flight Details")
    st.write(
        '<style>'
        'table {width: 100%; border-collapse: collapse;}'
        'th, td {border: 1px solid #ddd; padding: 8px;}'
        'th {background-color: #0066cc; color: white;}'
        'tr:nth-child(even) {background-color: #f2f2f2;}'
        'tr:hover {background-color: #ddd;}'
        '</style>',
        unsafe_allow_html=True
    )

    flight_table = st.empty()
    flight_table.table(pd.DataFrame(flight_details))

    # Get user input for customer type
    customer_type = st.radio("Select the customer type you are catering to:", ["Loyal Customer", "Non-Frequent Customer"])

    # Get user input for problem domains
    problem_domains = st.multiselect(
        "Select your problem domains:",
        ["Seat Comfort", "Inflight Entertainment", "Food and Drink", "On-time Performance", "Baggage Handling", "Online Booking"]
    )

    # Add a to-do list feature with checkboxes
    st.sidebar.title("To-Do List")
    todo_list = ["Check flight status", "Contact ground crew", "Schedule maintenance", "Review safety protocols"]
    todo_status = [False] * len(todo_list)
    for i, item in enumerate(todo_list):
        todo_status[i] = st.sidebar.checkbox(item, key=f"todo_{i}")

    # Add a calendar to track flights
    st.sidebar.title("Flight Calendar")
    today = datetime.today()
    month_days = calendar.monthcalendar(today.year, today.month)
    month_df = pd.DataFrame(month_days, columns=list(calendar.day_name))
    st.sidebar.table(month_df)

    # Add a submit button
    if st.button("Submit"):
        # Generate recommendations based on user input
        recommendations = generate_recommendations(customer_type, problem_domains)

        # Display the recommendations
        st.subheader("Here are the personalized recommendations that you can give to the customer you are serving to:")
        for problem_domain, recommendation in recommendations.items():
            st.subheader(f"{problem_domain}:")
            for rec in recommendation:
                st.write(rec)

# Function to display a motivational quote as a marquee
def display_marquee_quote():
    quote = random.choice(motivational_quotes)
    st.markdown(
        f'<marquee style="color:{secondary_color}; font-size:20px;">{quote}</marquee>',
        unsafe_allow_html=True
    )

# Define the main function to create the app
def main():
    # Set page config
    st.set_page_config(
        page_title="Airline Recommendation System",
        page_icon="✈️",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Set the title and description
    st.title("Welcome to Airline Recommendation System for FlightOps")
    st.subheader("Get personalized recommendations for your next flight Service!")

    # Display the marquee quote
    display_marquee_quote()

    # Display the dashboard
    show_dashboard()

# Run the main function to start the app
if __name__ == "__main__":
    main()
