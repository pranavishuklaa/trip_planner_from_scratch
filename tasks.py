# To know more about the Task class, visit: https://docs.crewai.com/concepts/tasks
from crewai import Task
from textwrap import dedent


class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def plan_itinerary(self, agent, city, travel_dates,interests):
        return Task(
            description=dedent(
                f"""
                    **Task**: Develop a 7 Day travel itinerary
                    **Description**: Expand the city guide into a full 7-day travel plan with detailed
                                    per-day plans, including weather forecasts, places to eat, packing suggestions, and budget breakdown
                                    You MUST actually suggest places to visit, actual hotes/resorts to stay and actual restaurents to go. 
                                    This itinerary should cover all aspects of the trip, from arrival to depataurter, integrating, the city 
                                    guide information with practical travel logistics.

                    **Parameters**: 
                    - City: {city}
                    - Trip Date: {travel_dates}
                    - Traveler Interests: {interests}

                    **Note**: {self.__tip_section()}


        """
            ),
          
            agent=agent,
        )

    def identify_city(self, agent,origin, cities, interests, travel_dates):
        return Task(
            description=dedent(
                    f"""
                        **Task**: Identify the Best City for the trip 
                        **Description**: Analyze and select the best city for the trip based on specific 
                                        criteria such as weather patterns, seasonal events, and travel costs
                                        This tasks involves comparing multiple cities , considering factors like current weather
                                        conditions, upcoming cultural/ sesonal events, and overall travel expenses 
                                        Your final answer must be detailed report on the chosen city,including actual flight costs, 
                                        weather forecasts and attractions. 

                        **Parameters**: 
                        - Origin: {origin}
                        - Cities: {cities}
                        - Trip Date: {travel_dates}
                        - Traveler Interests: {interests}

                        **Note**: {self.__tip_section()}
                    
        """
            ),
            expected_output="The expected output of the task",
            agent=agent,
        )
    

    def gather_city_info(self, agent, city, travel_dates,interests):
        return Task(
            description=dedent(
                f"""
                    **Task**: Gather In-depth City Guide Information
                    **Description**: Complie an in-depth guide for the selected city, gathering
                                    information about key attractions, local customs, special events, and daily activity recommendations.
                                    This guide should provide through a overview of what the city has to offer, including 
                                    hidden gems, cultural hotspots, must-visit, weater forecasts, and high level costs.


                    **Parameters**: 
                    - City: {city}
                    - Trip Date: {travel_dates}
                    - Traveler Interests: {interests}

                    **Note**: {self.__tip_section()}


        """
            ),
            
            agent=agent,
        )


