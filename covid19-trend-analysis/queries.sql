-- Top 10 countries by total cases
SELECT location, MAX(total_cases) AS max_cases
FROM covid_data
GROUP BY location
ORDER BY max_cases DESC
LIMIT 10;

-- Global daily cases
SELECT date, SUM(new_cases) AS global_cases
FROM covid_data
GROUP BY date
ORDER BY date;

-- Confirmed Cases and Deaths by Country

SELECT location, MAX(total_cases) AS max_cases, MAX(total_deaths) AS max_deaths
FROM covid_data
WHERE continent IS NOT NULL
GROUP BY location
ORDER BY max_cases DESC
LIMIT 10;


-- Global Time Trends
SELECT date, SUM(new_cases) AS global_cases, SUM(new_deaths) AS global_deaths
FROM covid_data
GROUP BY date
ORDER BY date;

-- Top 10 Countries by Total Cases
SELECT location, MAX(total_cases) AS max_cases
FROM covid_data
WHERE continent IS NOT NULL
GROUP BY location
ORDER BY max_cases DESC
LIMIT 10;

-- Global New Cases Over Time
SELECT date, SUM(new_cases) AS global_new_cases
FROM covid_data
GROUP BY date
ORDER BY date;

-- Daily Death Rate (Case Fatality Rate)
SELECT date, 
       SUM(new_deaths) * 1.0 / NULLIF(SUM(new_cases), 0) AS daily_death_rate
FROM covid_data
GROUP BY date
ORDER BY date;

-- Countries with the Most People Vaccinated
SELECT location, MAX(people_vaccinated) AS vaccinated
FROM covid_data
WHERE continent IS NOT NULL
GROUP BY location
ORDER BY vaccinated DESC
LIMIT 10;

-- TIME SERIES / TREND ANALYSIS
-- Monthly Total Cases for a Specific Country (e.g., United States)
SELECT 
    SUBSTR(date, 1, 7) AS month, 
    SUM(new_cases) AS monthly_cases
FROM covid_data
WHERE location = 'United States'
GROUP BY month
ORDER BY month;

-- Top 5 Deadliest Days Globally
SELECT date, SUM(new_deaths) AS global_deaths
FROM covid_data
GROUP BY date
ORDER BY global_deaths DESC
LIMIT 5;


-- Compare Cases vs. Deaths for a Country (India)
SELECT location, MAX(total_cases) AS total_cases
FROM covid_data
WHERE total_cases > 1000000 AND continent IS NOT NULL
GROUP BY location
ORDER BY total_cases DESC;



-- Top 10 Countries by Total Deaths per Population
SELECT 
    location,
    MAX(total_deaths * 1.0 / population) AS deaths_per_person
FROM covid_data
WHERE population IS NOT NULL AND continent IS NOT NULL
GROUP BY location
ORDER BY deaths_per_person DESC
LIMIT 10;

