# SafeZone EMS
> This project is dedicated to Hurricane Florence Victims and Victims of other such natural disasters

## Description
The objective of this system is to provide a more robust management/warning system for organizations who manage emergencies on a large scale. Examples of typical program deployment would be:
- Hurricanes
- Tsunamis
- Volcanoes
- Forest Fires
- Tornadoes
- etc.

The system is designed with versatility and mobility in mind allowing large organizations to be more efficient in communication and management of resources. The system allows for clear communication between large chains of command from the top of the totem pole to the bottom. We hope that this web app will enable organizations to manage their resources more effectively and ultimately prevent loss of life and lead to better outcomes over time leading to greater social good.

## APIs Integrated
- Google Maps API
- Google Geolocation
- Weather Terrapin (Storm Tracking)

## Features
- Through better preparedness and real time updates every 2 seconds, the web app keeps anyone (with access) up to date on the latest status updates and provides for real-time situational awareness.
- The server also actively tracks the storm as it progresses and updates all internal calculations on the fly!
- The web app responsive (_browser and mobile friendly_) allowing the reporting of information with/without power as long as any source of internet is available whether it be satellite internet, cell towers, or cable/dsl internet.
- The web app democratizes the management of resources and materials allowing for accurate data to be reported instead of information being relayed up and down the chain of command in a game of telephone.

Let's apply this app to the ***Hurricane Florence***. The web app allows for tracking of vital information at any number of safe zones that may have been setup. Each SafeZone has a manager who is in charge of the facility and the resource management at the facility. Each manager can effortlessly update the status of:
- Food
- Water
- Electricity
- Threat Assessment (Ex: How far away is the SafeZone from the eye of the storm)
- Status Updates
- Threat Toggling with smart analysis
- Medicine
- Resource Requisitions with urgency toggling
- Viability of current SafeZones based on various factors

The collective reporting of every manager can be viewed by a person at the top of the chain of command in charge of the emergency operations. So for example, the director of FEMA can view the needs and status of every zone without having to answer phone calls and replying to emails! 

## Screenshot
**Desktop View** | **Mobile Zone View**
--- | ---
![SafeZone - Desktop View](/screenshots/desktop.png "SafeZone - Desktop View") | ![SafeZone - Mobile Zone View](/screenshots/phone-modal.png "SafeZone - Mobile Zone View")

## Instructions:
- Upon loading the front page, the user is greeted by a screen that has a panel for zone setup and a panel on the lower with a map showing the eye of the storm relative to the safe zones.
- As safe zones are compiled by the user, custom markers are placed on the map using the Google Cloud Platform APIs for Google Maps.
- These markers are placed relative to the storm so the user can view the storm's location relative to the SafeZones setup.
- If a user attempts to setup a SafeZone they will be asked to fill out a simple form which gathers the necessary data for that location.
- From this information, the bird's eye status view is controlled.
- Based on critical thresholds, the zone will be colored based on it's current level of viability:
  - ***Green*** - The zone is in an optimal condition and little to no intervention is required.
  - ***Yellow*** - The zone requires attention but is of no immediate concern.
  - ***Red*** - Urgent intervention is required by the agency handling the situation to maintain the operation of that particular SafeZone. *More importantly, if the user uses any part of the following words in their status such as: `Urgent, Must, and Desperate`, the Zone will automatically be toggled to a red color marking it as urgent attention required.*
	
By selecting each zone, the director in charge of appropriation of resources or the individual in charge of the collective zones can view information about the quantity/status of each resource and any status updates the Zone manager might have placed.
- Aerial distance from the SafeZone to the threat. This is important since this distance is calculated for any number of zones that are being tracked by the program. This allows for important decisions to be made regarding the status of the zone and whether emergency evacuations should commence should the premises no longer remain safe or are projected to no longer be safe as they were earlier. 

- The page refreshes zone data every 2 seconds, so that viability status is available as soon as possible
- The hurricane location is updated real time when the server is initiated. The coordinates for epicenter data are fetched from: https://weather.terrapin.com/wx/storm_show.jsp?area=ATL&storm=06A&dtype=ASCII .


## Final thoughts
It is our sincere hope that this app enables the efficient management of large scale emergency management. This is just a proof of concept but it shows the real power and possibilities as well as the numerous advantages it would afford any organization in charge of tasks as important as these: Saving lives.

---
***Authors:*** Lead Developer(front end, back end, algos, styling): [_**@avdaredevil**_](https://github.com/avdaredevil) || (Project Lead,Integrated Google APIs, Front End, Styling) [_**@tvdaredevil**_](https://github.com/tvdaredevil), Other Devs(Back End & Algos): [_**@karim-salem**_](https://github.com/karim-salem), [***Vladyslav Kuz***](https://github.com/vladk97)
