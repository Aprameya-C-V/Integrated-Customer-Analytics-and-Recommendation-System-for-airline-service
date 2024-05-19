import streamlit as st
import random

# Define airline-themed colors
primary_color = '#0066cc'  # Blue
secondary_color = '#ffcc00'  # Yellow
text_color = '#333333'  # Dark Gray

# Define flight details
flight_details = [
    {"Flight No": "ABC123", "Departure": "New York", "Destination": "Los Angeles", "Departure Time": "08:00 AM",
     "Arrival Time": "10:00 AM", "Gate": "A1", "Status": "On Time"},
    {"Flight No": "DEF456", "Departure": "Los Angeles", "Destination": "Chicago", "Departure Time": "11:00 AM",
     "Arrival Time": "01:00 PM", "Gate": "B2", "Status": "Delayed"},
    {"Flight No": "GHI789", "Departure": "Chicago", "Destination": "Houston", "Departure Time": "02:00 PM",
     "Arrival Time": "04:00 PM", "Gate": "C3", "Status": "On Time"},
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

# Function to display the dashboard after successful login
def show_dashboard():
    # Display user profile information
    st.sidebar.title("User Profile")
    st.sidebar.image("Flightops1.png", use_column_width=True)
    st.sidebar.subheader("Name:")
    st.sidebar.write("Aprameya")
    st.sidebar.subheader("Designation:")
    st.sidebar.write("FlightOps Manager")
    st.sidebar.subheader("Location:")
    st.sidebar.write("Headquarters")

    # Display flight details table with enhanced styling
    st.subheader("Next Flight Details")
    flight_table = st.empty()
    flight_table.write("Flight No\tDeparture\tDestination\tDeparture Time\tArrival Time\tGate\tStatus")
    flight_table.write("--------\t----------\t------------\t--------------\t------------\t----\t------")
    for flight in flight_details:
        status_color = "green" if flight["Status"] == "On Time" else "red"
        flight_table.write(f"{flight['Flight No']}\t{flight['Departure']}\t{flight['Destination']}\t"
                           f"{flight['Departure Time']}\t{flight['Arrival Time']}\t{flight['Gate']}\t"
                           f"<span style='color:{status_color}'>{flight['Status']}</span>", unsafe_allow_html=True)

    # Get user input for customer type
    customer_type = st.radio("Select the customer type you are catering to:", ["Loyal Customer", "Non-Frequent Customer"])

    # Get user input for problem domains
    problem_domains = st.multiselect(
        "Select your problem domains:",
        ["Seat Comfort", "Inflight Entertainment", "Food and Drink", "On-time Performance", "Baggage Handling", "Online Booking"]
    )

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

    # Display account credentials
    st.sidebar.title("Account Credentials")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    login_button = st.sidebar.button("Login")

    # Dummy authentication (replace with actual authentication logic)
    if login_button:
        if username == "aprameya1" and password == "123456":
            st.success("Login successful!")
            show_dashboard()
        else:
            st.error("Invalid username or password. Please try again.")

# Run the main function to start the app
if __name__ == "__main__":
    main()
