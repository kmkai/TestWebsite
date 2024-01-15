import streamlit as st
import pandas as pd

def display_activities(day):

    if day == '':
        st.write("I 1953 tok Oriana og Enrico Panattoni, et par toskanske innvandrere, over en kafé. De introduserte en unik suppe i kafeen sin, kalt 'stracciatella', som var en blanding av buljong og pisket egg.")

        st.write("Inspirert av denne suppen, begynte Enrico å eksperimentere. Han laget en myk krem av melk og helte deretter flytende mørk sjokolade over. Den varme sjokoladen 'rev seg selv opp' ved kontakt med den kalde kremen, på samme måte som stracciatella-suppen. Dette var begynnelsen på stracciatella-is, en oppfinnelse som tilfeldigvis endret iskremens verden for alltid.")

        st.write("Og nå kommer overraskelsen: Vi skal besøke Ristorante La Marianna i Bergamo for å smake på denne originale stracciatella-isen.")
        

    elif day == 'tickets':
        # Airplane Tickets
        st.subheader('Airplane Tickets')
        with st.expander('Oslo Torp to Milan Bergamo'):
            st.write('Date: January 15, 2024')
            st.write('Gate Close: 09:25')
            st.write('Departure Time: 09:55')
            st.write('Departure Airport: Oslo Torp')
            # ... add other details as needed
            st.image('images/Boarding-pass1.png')  # Replace with your actual image URL
            st.image('images/Boarding-pass2.png')  # Replace with your actual image URL

        with st.expander('Milan Bergamo to Oslo Torp'):
            st.write('Date: January 21, 2024')
            st.write('Gate Close: 14:20')
            st.write('Departure Time: 14:55')
            st.write('Departure Airport: Milan Bergamo')
            # ... add other details as needed
            # st.image('images/Boarding-pass1.png')  # Replace with your actual image URL
            # st.image('images/Boarding-pass2.png')  # Replace with your actual image URL

        st.subheader('Bus Ticket to hotel')
        with st.expander('Bus Ticket'):
            st.write("To get to Porta San Giacomo from Milan Bergamo Airport, you can take the bus with a sign beside it saying number 1.")
            st.write("You will go out at a place called Viale delle Mura 40 S.Giacomo.")
            st.write("The bus ticket costs 2.50€ and you can buy it on the bus. The bus ride takes about 30 minutes.")
            st.write("Here is the Google Maps link for the route:")
            st.markdown(f"[Open Google Maps](https://www.google.com/maps/dir/Bergamo+%2F+Orio+al+Serio+Airport+(BGY),+Via+Aeroporto,+Orio+al+Serio,+Province+of+Bergamo,+Italy/Porta+San+Giacomo,+Via+Sant'Alessandro,+73,+24121+Bergamo+BG,+Italy/@45.6846884,9.6645461,14z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x4781506f9e32830d:0x177c7faf1030082!2m2!1d9.7074056!2d45.668978!1m5!1m1!1s0x47815114e9dc2833:0xeda380eefc31254a!2m2!1d9.6630287!2d45.7012292!3e3?entry=ttu)", unsafe_allow_html=True)
            st.write("First image is the buss stop:")
            st.image('images/e.png')
            st.image('images/ew.png')

            
        st.subheader('Hotel Bookings')

        # Hotel Booking Expander
        with st.expander('Monday to Wedensday'):
            st.write('Date: January 15 - January 17')
            st.write('Estimated time of arrival: 14:00')
            st.write('Hotel Name: B&B San Lorenzo Bergamo')
            st.write('Address: Via Gombito 4, Bergamo')
            st.markdown(f"[Open Google Maps](https://www.google.com/maps?q=Via+Gombito+4,+Bergamo)", unsafe_allow_html=True)
            st.subheader('Access Instructions')
            st.image('images/Hotel11.jpg')  # Replace with the actual image URL or path

            st.write("When you arrive at the front entrance of Via Gombito 4, as shown in the image over, enter the following access code on the keypad:")
            st.write("**Access Code:** 1168")
            st.write("After entering through the door, you will find yourself inside the courtyard of the palace. Then you go to the staircase and go in that door which is always open. The entrance door to B&B San Lorenzo is on the first floor, after the staircase.")
            st.image('images/Hotel1.jpg')  # Replace with the actual image URL or path
            st.write("To log in, simply enter the following code on the keypad:")
            st.write("**Login Code:** 202301#")
            st.write("Use the same code to open the door to the room you have booked:")
            st.write("**Room Name:** DON PASQUALE")
            st.image('images/ticket.png')  # Replace with the actual image URL or path

        st.subheader('Hotel Bookings')

        # Hotel Booking Expander
        with st.expander('Milan Royal Suites - Centro Brera'):
            st.write('Date: January 17 - January 18')
            st.write('Estimated time of arrival: 15:00-16:00')
            st.write('Hotel Name: Milan Royal Suites Centro Brera')
            st.write('Address: Via dell Orso 20, 20124 Milan')
            st.subheader('Access Instructions')
            st.image('images/Hotel11.jpg')  # Replace with the actual image URL or path
            st.write('This artpartment are located close to Milan Centro Brera, we have other arpartments that are located in Milano, so if any doubt you can use same address to find it. Via dell Orso 20, 20124 Milan')

        st.subheader('Hotel Bookings')

        # Hotel Booking Expander
        with st.expander('Casa Mario Lupo - Apartments and Rooms'):
            st.write('Date: January 18 - January 21')
            st.write('Estimated time of arrival: 15:00-16:00')
            st.write('Hotel Name: Casa Mario Lupo - Apartments and Rooms')
            st.write('Address: Via Mario Lupo 12, 24129, Bergamo')
            st.subheader('Access Instructions')
            st.image('images/Hotel11.jpg')  # Replace with the actual image URL or path
            st.write('To check in you will go to the shop called Prelibastessen. It is in Via Mario lupo 12 A. Here you will meet the owner that will help you. You will also need to pay local tax for the stay, that will be in total 24 euro and be payed in cash to owner when checking in.')
        
        # Opera Ticket details
        st.subheader('Opera Ticket')
        with st.expander('Opera Médée Turno A'):
            st.write('Date: January 17, 2024')
            st.write('Time: 20:00')
            st.write('Enjoy a night at the opera in Milan!')
            st.image('images/icket1.png')
            st.image('images/icket2.png')
            st.write('Seating: Palchi Zona 1')
            st.write('Seat 1: PALCO II ORDINE SX n. 3 Posto 1')
            st.write('Seat 2: PALCO II ORDINE SX n. 3 Posto 2')

    elif day == 'Monday':
            st.success('Du vil sjekke inn på det nye hotellet på mandag.')

            st.image('images/La Rocca.jpg')
            with st.expander('Aktivitet 1: La Rocca'):
                st.write('Utforsk den historiske festningen La Rocca, som tilbyr fantastisk panoramautsikt over Bergamo og omgivelsene.')
                st.write('Du kan gå inn i museet for å lære mer om det og også gå opp på toppen av festningen. Ved siden av kan du gå inn i denne vakre parken - et minnesmerke for de falne i første og andre verdenskrig.')
                st.image('images/La Rocca.jpg')
                st.markdown(f"[Open Google Maps](https://www.google.com/maps?q=La+Rocca,+Bergamo)", unsafe_allow_html=True)

            st.image('images/Colleoniapel.jpg')
            with st.expander("Aktivitet 2: Colleoni's Kapell"):
                st.write("Oppdag det vakre Colleoni's Kapell, et mesterverk av renessansearkitektur prydet med intrikate dekorasjoner.")
                st.image('images/Colleoniapel.jpg')
                st.markdown(f"[Open Google Maps](https://www.google.com/maps?q=Colleoni's+Chapel,+Bergamo)", unsafe_allow_html=True)

            st.image('images/Piazza Vecchia.jpg')
            with st.expander("Aktivitet 3: Piazza Vecchia"):
                st.write("Beundre den vakre plassen, hvor du vil se Civic Tower. Et tårn du kan gå opp i og se hele byen. Du vil også se Basilica di Santa Maria Maggiore, en vakker kirke. Det anbefales å dra om kvelden for å se solnedgangen. Åpningstidene er fra 10:00 til 18:00.")
                st.image('images/Piazza Vecchia.jpg')
                st.markdown(f"[Open Google Maps](https://www.google.com/maps?q=Basilica+di+Santa+Maria+Maggiore,+Bergamo)", unsafe_allow_html=True)

            st.image('images/mura.jpg')
            with st.expander('Aktivitet 4: Bergamos murer'):
                st.write('Utforsk de historiske murene i Bergamo, som omgir den gamle byen og tilbyr panoramautsikt over byen.')
                st.write('Du kan gå langs murene og nyte den vakre naturen. Du kan besøke Porta San Giacomo, en av hovedportene til murene.')
                st.image('images/mura.jpg')
                st.markdown(f"[Open Google Maps](https://www.google.com/maps?q=Walls+of+Bergamo)", unsafe_allow_html=True)


            # Sample Data
            restaurants = [
                ("Pizzeria Assaje Bergamo", "Savor delicious pizza at Pizzeria Assaje Bergamo.", "Its Milano pizza and the best pizzaria in the Bergamo, you can find all the different recipes on their menu online, you will have to clik on menu to get a list, you can click on different names in list and it will show more, and you can go click again on menu to get list and click on new name to see more recipes they make see more and then you can choose more different types of pizza they make https://www.assaje.it/menu/carta-delle-margherita/", "https://www.google.com/maps?q=Pizzeria+Assaje+Bergamo"),
                ("La Marianna", "Indulge in creamy stracciatella ice cream at La Marianna.", "","https://www.google.com/maps?q=La+Marianna,+Bergamo"),
                ("Circolino Città Alta", "Enjoy Italian cuisine with a view at Circolino Città Alta.","", "https://www.google.com/maps?q=Circolino+Citt%C3%A0+Alta,+Bergamo"),
                ("Da Mimmo Bergamo Alta", "Try traditional dishes at Da Mimmo Bergamo Alta.","", "https://www.google.com/maps?q=Da+Mimmo+Bergamo+Alta"),
                ("Carmen", "Amazing ice cream at Carmen.","", "https://www.google.com/maps?q=Carmen,+Bergamo"),
                ("Mimì • La Casa dei Sapori", "Experience traditional Italian flavors at Mimì • La Casa dei Sapori.", "","https://www.google.com/maps?q=Mim%C3%AC+%E2%80%A2+La+Casa+dei+Sapori,+Bergamo"),
                ("Ristorante la Tana", "Enjoy classic Italian cuisine at Ristorante la Tana.","", "https://www.google.com/maps?q=Ristorante+la+Tana,+Bergamo")
            ]

            # Streamlit App
            def main():
                st.title('Restaurants in Bergamo')

                for name, description, about, maps_link in restaurants:
                        st.subheader(description)
                        with st.expander("Info"):
                            st.write(about)
                            if st.button("View on Maps", key=name):
                                st.markdown(maps_link, unsafe_allow_html=True)

            if __name__ == "__main__":
                main()



    elif day == 'Tuesday':
        st.subheader('Activities for Tuesday')
    elif day == 'Wednesday':
        st.success('You will book into new hotel on Monday. You have a ticket for the opera 8. From hotel to opera is 10 minutes by foot.')

        st.subheader('Activities for Wednesday')
        st.image('https://source.unsplash.com/featured/?bergamo')
        with st.expander('Activity 1: Explore Milan Cathedral'):
            st.write('Visit the iconic Milan Cathedral, a masterpiece of Gothic architecture.')
            st.image('https://source.unsplash.com/featured/?milan-cathedral')
            st.markdown(f"[Open Google Maps](https://www.google.com/maps?q=Milan+Cathedral)", unsafe_allow_html=True)

        st.image('https://source.unsplash.com/featured/?san-vigilio')
        with st.expander('Activity 2: Visit Teatro alla Scala'):
            st.write('Explore the historic Teatro alla Scala, one of the worlds most famous opera houses.')
            st.image('https://source.unsplash.com/featured/?teatro-alla-scala')
            st.markdown(f"[Open Google Maps](https://www.google.com/maps)", unsafe_allow_html=True)
        
                # Sample Data
        restaurants = [
            ("Pizzeria Assaje Bergamo", "Savor delicious pizza at Pizzeria Assaje Bergamo.", "It have best pizza and here is link to there menu https://www.assaje.it/menu/pizze-tradizionali/", "https://source.unsplash.com/featured/?milan-cathedral", "https://www.google.com/maps?q=Pizzeria+Assaje+Bergamo"),
            ("La Marianna", "Indulge in creamy stracciatella at La Marianna.", "ok","https://source.unsplash.com/featured/?milan-cathedral","https://www.google.com/maps?q=La+Marianna,+Bergamo"),
            # ... add other restaurants here
        ]

        # Streamlit App
        def main():
            st.title('Restaurants in Milan')

            for name, description, about, image, maps_link in restaurants:
                    st.subheader(description)
                    with st.expander("Info"):
                        st.write(about)
                        st.image(image)
                        if st.button("View on Maps", key=name):
                            st.markdown(maps_link, unsafe_allow_html=True)

        if __name__ == "__main__":
            main()
        # Restaurants in Milan
        st.subheader('Restaurants in Milan')
        st.write('1. **Italian Restaurant:** Enjoy authentic Italian cuisine at a local restaurant. [Google Maps](https://www.google.com/maps?q=Italian+Restaurant,+Milan)')
        st.write('2. **Pizza Place:** Savor delicious pizza at a pizzeria in Milan. [Google Maps](https://www.google.com/maps?q=Pizza+Place,+Milan)')



    elif day == 'Thursday':
        st.subheader('Activities for Thursday')
    elif day == 'Friday':
        st.subheader('Activities for Friday')
    elif day == 'Saturday':
        st.subheader('Activities for Saturday')
    elif day == 'Sunday':
        st.subheader('Activities for Saturday')

# Main program
days = ['','tickets', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
selected_day = st.selectbox('',days)
display_activities(selected_day)


