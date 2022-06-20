import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    cities_available = ['chicago', 'washington', 'new york']

    while True:
        city = input('Kindly input the city data you want to analyse from washington, new york and chicago \n').lower()
        if city in cities_available:
            break
        else:
            print('You entered an invalid city')

    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ['january', 'february', 'March','april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    month_dec = input('Are you analyzing all month or a specific month?\nPlease enter Yes for all').lower()
    if month_dec == 'yes':
        month = 'all'
    else:
        while True:
            month = input('The month you\'d like to analyze? \nPlease enter the month in full\n').lower()
            if month in month_list:
                break
            else:
                print('please enter a valid month')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = int(input('Please enter the day you want to analyze. Enter 1 = sunday, 2 = monday,..., 7 = saturday\n'))
            if 1 <= day <= 7:
                break
            else:
                print('out of range!')
        
        except:
            print('You entered an invalid day!')

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['Week Day'] = df['Start Time'].dt.dayofweek
    df['Hour'] = df['Start Time'].dt.hour
    mon_index = {'january': 1, 'february': 2, 'March': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}
    if month != 'all':
        df = df.loc[df['month'] == mon_index[month]]
    if day != 'all':
        day -= 1
        df = df.loc[df['Week Day'] == day]

   

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_month = df['month'].mode()
    print(most_month)

    # TO DO: display the most common day of week
    most_weekday = df['Week Day'].mode()
    print(most_weekday)

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    most_hour = df['Hour'].mode() 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].mode()
    print(most_start_station)

    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].mode()
    print(most_start_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start to End'] = df['Start Station'] + '-' + df['End Station']
    most_start_end = df['Start to End'].mode()
    print(most_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print(total_time)

    # TO DO: display mean travel time
    average_time = df['Trip Duration'].mean()
    print(average_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    print(user_count)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print(gender_count)
    else:
        print('gender is not available!')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        print(earliest_year)
        youngest_year = df['Birth Year'].max()
        print(youngest_year)
        most_common_year = df['Birth Year'].mode()
        print(most_common_year)
    else:
        print('birth year data is not avaiable!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_five(df):
    """Displays 5 rows of the data"""
    view_data = input('Would you like to view the first 5 rows?\n').lower()
    if view_data == 'yes':
        i = 0
        while 0 < 1:
            print(df.loc[i:i + 5])
            i+=5
            output_result = input('Would you like to view the next 5 rows?\n').lower()
            if output_result != 'yes':
                break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_five(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
