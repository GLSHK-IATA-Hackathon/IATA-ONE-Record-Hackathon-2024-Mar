# IATA-ONE-Record-Hackathon-2024

**Inspiration**

In today's eCommerce-driven world, the increasing volume of goods being transported via air cargo poses challenges for supply chain stakeholders in identifying and uncovering unregulated DG items. This presents risks to property and lives. Traditional methods of visual inspection and documentation checks may overlook hidden DG items, and a lack of DG knowledge may result in undetected hazardous goods.

Additionally, there are limitations in information sharing between stakeholders in the air cargo supply chain, particularly in the context of eCommerce. Shippers possess detailed item information but struggle to share it with airlines, resulting in extensive manual data entry for airline staff. Shippers also face difficulties in tracking shipment status at the item level.

Challenges addressed:
- Identifying and uncovering hidden DG goods.
- Facilitating information sharing between air cargo supply chain stakeholders.
- Enabling track and trace capabilities at the piece level.
- Allowing non-registered parties to benefit from OneRecord.

**Your solution and what it does**

Our solution leverages advanced technology, specifically AWS machine learning services, to address the hidden DG item issue. We incorporate this technology to recognize goods descriptions that may indicate potential DG items.

Within our solution, we provide a CSV upload function for shippers to upload piece information. Our application converts the piece information into piece LO (Logistic Object) and stores it in the One Record Server. Simultaneously, our system utilizes AWS machine learning services to identify any DG warnings for the uploaded pieces. Agents can quickly see if there are DG items and reuse the piece LO to create bookings with airlines, eliminating the need for time-consuming data entry. Furthermore, the piece LO is bound to the booking LO in OneRecord, allowing shippers to track shipment statuses using the piece ID.

**How did you build it?**

We built our solution by prototyping the Text Classification using AWS SageMaker for detecting hidden DG, through goods description, special handling codes, shipper, and consignee details. The AI shall be trained using BlazingText algorithm, “DG category” will be spotted out and shown in our solution. Besides NE:One Server and NE:One Play, we employed Vue.js and .net core in building our solution, enabling the pieces LOs creation through CSV upload and pieces link up master AWB.

**What are you proud of?**

Through the adoption of our solution, all stakeholders in the air cargo supply chain can more easily identify and uncover hidden DG items. Information sharing becomes seamless, and airline users can quickly confirm bookings without extensive data input. Shippers gain the ability to track each piece's status without relying on AWB (Air Waybill) numbers. As a result, the air cargo supply chain becomes safer and more efficient.

We aim to not only protect lives but also instill confidence in air cargo transportation. We see this as a revolutionary step forward for the industry.

**What is next step for your solution and how will you take that step?**

Our System can be used for classic booking now. We will further enhance it to support modern booking flow that enables users to send booking option request to airline and select the booking option they prefer.

We also want to apply AWS machine learning model to recognize fake documents, e.g., MSDS, UN38.3 report. Moreover, DG detection feature could be applied in airline system, helping on shipment acceptance and etc. So that we can also reduce the potential risks from DG shipments.

