# Energy Insights 360

<div align="center">
<img src="https://github.com/user-attachments/assets/19cb02cf-898d-4bea-9494-e9bab98fe3d1" alt="Description of image" >
</div>



- **Author(s):** Taissir Boukrouba
- **Affiliation:** Personal Project  
- **Date:** 11/2024

---




## Project Overview 
**Energy Insights 360** is an interactive dashboard for EU fuel statistics, which makes it easy to understand fuel dynamics in the main fuel types (crude oil, coal, lignite, and natural gas) across different regions. This project aims at supporting the EU member states stakeholders by giving them sector-specific information, environmental implications, and visualizations that make it easier to comprehend the usage of energy across industries. Along with that, *Energy Insights 360* stands out from traditional dashboards due to its storytelling feature that allows the users to go through different scales: from global trends down to company and region insights. By starting with global energy consumption statistics, the narrative gives a grasp of the EU's position among other countries which will be followed by an analysis of the oil-producing companies as well as regional differences in using coal, lignite, and natural gas. This is a multi-level strategy that ensures, users not only can see the EU's fuel statistics but also related to how these patterns are located in the broader context of, therefore, they will have knowledge and skills for development and implementation across green and economic fields.




## Methodology
### Data Preprocessinng : 
> [!IMPORTANT]  
> You can check the data files inside the [data directory](/data/)

The data preprocessing phase was essential for transforming the original dataset, which consisted of multi-sheet Excel files containing related but distinct fuel statistics. To streamline the analysis process, each sheet was separated, allowing for individual examination and cleaning. This included identifying inconsistencies, removing duplicates, and addressing any missing values to ensure data quality and integrity.
After cleaning, the processed data from each sheet was combined into a single CSV file, with each sheet represented as a separate feature. This conversion not only simplified data handling but also enhanced compatibility with various data analysis tools. By the end of this phase, the dataset was ready for further analysis, enabling the project to effectively derive insights into fuel statistics across the EU and beyond.


![eneregy 360](https://github.com/user-attachments/assets/9bf542e9-da2a-4ce7-9620-082939d9c10c)

### Dashboarding : 
> [!IMPORTANT]  
> You can check the plots whithout the platform inside the [plots directory](/plots/)

During the dashboarding phase, the unified CSV served as the foundational dataset for creating a comprehensive visualization platform that transformed raw data into meaningful insights. Key performance indicators (KPIs) reflecting critical trends in fuel statistics were derived through various calculations, including total fuel consumption, emissions estimates, and regional comparisons. The dashboard was designed for optimal representation of these KPIs, facilitating quick comprehension of complex data relationships. To enhance user engagement, a set of interactive widgets—such as charts and graphs—was developed, allowing users to filter and drill down into specific areas of interest, including time trends and sector-specific usage patterns.The result was a dynamic dashboard that effectively visualized data and provided actionable insights into EU fuel dynamics. Users could explore the data interactively, leveraging the custom functions and computations that enriched the widgets for deeper insights into the energy landscape. The following diagram summarises its structure : 

<br>

<div align="center">
<img src="https://github.com/user-attachments/assets/3029906b-ae58-4a20-8974-fbab566006f9"  width=600 >
</div>




## Dashboard Features 
The Energy Insights 360 dashboard is designed to showcase fuel statistics specific to the EU through a range of interactive and visually appealing widgets, making complex data easy to understand and actionable for users:

- **Gauge Plots and KPI Cards :** These tools highlight key performance indicators (KPIs) such as load factor, energy intensity, and annual trade metrics, providing users with a quick overview of essential metrics at a glance.
- **Pie Charts for Fuel Contribution:** Pie charts illustrate the contributions of different energy sources—such as coal, natural gas, and renewables—allowing users to visualize the share of each fuel type in the EU's overall energy mix.
- **Line Plots Trends & Comparisons**: Time series and bar charts display trends in fuel usage and emissions over time, along with comparative data across various regions and sectors within the EU.

Each widget and chart is crafted to provide a targeted view of specific KPIs, allowing users to engage with the data and explore details for a more comprehensive understanding of EU fuel dynamics. Collectively, these visualizations facilitate data-driven insights into energy efficiency, trade intensity, and sustainability within the EU framework.
### Dashboard KPIs 

| KPI                       | Definition                                                                                                 |
|---------------------------|------------------------------------------------------------------------------------------------------------|
| **Load Factor**           | A measure of the efficiency of energy generation, calculated as the ratio of actual output to potential output over a specific period. |
| **Average Annual BOT**    | Refers to the average annual Bill of Trade, which represents the average value of imports and exports in energy resources over a year. |
| **Coal Discrepancy**      | The difference between reported coal production or consumption and the actual measured amounts, highlighting inconsistencies in coal data reporting. |
| **Intensity of Trade**    | A metric that assesses the volume of trade relative to economic output, often measured in terms of energy trade volume per unit of GDP. |
| **Energy Contribution**   | The percentage contribution of various energy sources (e.g., coal, natural gas, renewables) to the total energy supply of a specific region or country. |
| **Balance of Trade**      | The net difference between the value of energy exports and imports, indicating whether a region is a net importer or exporter of energy resources. |




## Data Narrative 

Beyond providing EU-specific statistics, this project distinguishes itself with a unique data narrative that extends from global to regional insights. Recognizing that energy dynamics are interconnected across different levels, Energy Insights 360 introduces a structured narrative that progresses through three levels of analysis:

- **Global Layer:** Sets the stage by examining worldwide energy consumption patterns, illustrating how the EU’s energy profile fits within broader global trends.
- **Organizational Layer:** Focuses on crude oil usage within EU-based organizations, showcasing organizational roles in production and distribution. This level emphasizes how companies contribute to and are impacted by EU energy policies and global shifts in oil production.
- **Regional Layer:** Narrows down to specific EU regions, providing detailed insights into coal, lignite, and natural gas consumption. This localized view helps stakeholders understand how regional fuel dynamics differ and how they contribute to the EU's overall energy landscape.
  
Each layer in the narrative provides contextual explanations and highlighted insights, guiding users through the flow from global trends to regional details. This structure ensures that stakeholders can move seamlessly from understanding the broader energy context to drilling down into specific, actionable regional data.


## Depolyement 

The *Energy Insights 360* project is deployed using **Streamlit** and hosted on **GitHub Pages**, making it accessible directly from any web browser. Here’s an overview of the deployment process:

1. **Building with Streamlit**: Streamlit, a Python-based framework, powers the interactive dashboard, allowing users to explore KPIs, gauge plots, and other charts on EU fuel statistics. Streamlit’s widgets and real-time data display capabilities create a responsive, user-friendly interface for data exploration.

2. **Setting Up GitHub Repository**: The project code, data files, and dependencies are stored in a GitHub repository, enabling version control and public accessibility. This setup also allows for collaborative development and simplified updates.

3. **Hosting with GitHub Pages**: Although Streamlit apps are typically hosted on dedicated platforms, this project leverages GitHub Pages for deployment. A tool like **Streamlit-Static** can be used to convert the app for static hosting, or the app can be containerized and updated via **GitHub Actions**.

4. **Automated Deployment with GitHub Actions**: GitHub Actions enables automated CI/CD, so each update to the main branch triggers a redeployment on GitHub Pages. This ensures that the dashboard is always up-to-date with the latest code and data.

5. **User Accessibility**: The deployed dashboard is accessible through a GitHub Pages URL, allowing users to interact with real-time data visualizations from any device. The combination of Streamlit’s interactivity and GitHub Pages’ easy access provides a seamless experience for analyzing EU energy metrics.

This setup ensures a robust, accessible, and constantly updated dashboard for exploring energy insights.
