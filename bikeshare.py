import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
weekday = ['sunday','monday','tuesday', 'wednesday','thursday','friday','saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington? \n")
        if city.lower() not in CITY_DATA:
            print("invalid inputs")
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter the name of the month to filter by, or all to apply no month filter ? \n").lower()   
        if month.lower() not in months and month.lower() != 'all':
            print("invalid inputs")
        
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter the name of the day of week to filter by, or all to apply no day filter ? \n")   
        if day.lower() not in weekday and day.lower() != 'all':
            print("invalid inputs")
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    if city == 'chicago':
       df = pd.read_csv('chicago.csv')
    elif city == 'new york city':
        df = pd.read_csv('new_york_city.csv')

    else:
        df = pd.read_csv('washington.csv')
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('The Most Common Month:', common_month)

    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['week'] = df['Start Time'].dt.week
    common_week = df['week'].mode()[0]
    print('The Most Common Week:', common_week)


    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The Most Common Hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()
    print('The Start Station:', start_station) 
    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()
    print("The End Station: ", end_station) 
    # TO DO: display most frequent combination of start station and end station trip
    frequent_station = (df['Start Station'] + '' + df['End Station']).mode()
    print("The Frequent Station: ",  frequent_station) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(pd.Series([(df['Trip Duration']).sum(), 
                      ], 
                     index=['Total Time:']))
    
    # TO DO: display mean travel time
    print(pd.Series([(df['Trip Duration']).mean(), 
                      ], 
                     index=['Average Time:']))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user = df['User Type'].count()
    print("The user counts:",user)

    # TO DO: Display counts of gender
    if df['Gender'].isnull().all():
        pass
    else:
        gender = df['Gender'].count()
        print("The gender counts:", gender)
   

    # TO DO: Display earliest, most recent, and most common year of birth
    year = df['Birth Year'].max()
    

    print("The most recents year:", int(year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 5
    while (view_data.lower() == 'yes'):
        print(df.iloc[:start_loc])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
def main():
    try : 
        while True:
            city, month, day = get_filters()
            df = load_data(city, month, day)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            display_data(df)
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
	main()
