#! /opt/conda/bin/python

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
    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("enter any city (chicago, new york city or washington): ").lower()
        if city in ['chicago' , 'new york city' , 'washington']:
            break
    
    

    # Get user input for month (all, january, february, ... , june)
    while True:
        month = input ("enter month (all, january, february, ... , june): ").lower()
        if month in ['all','january','february', 'march', 'april', 'may' , 'june']:
            break
    
    

    # Get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input ("enter day: ").lower()
        if day in ['all','monday','tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']:
            break
    
    print("\nChosen City: %s" % city)
    print("Chosen Month: %s" % month)
    print("Chosen Day: %s" % day)

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

    df = pd.read_csv('{}.csv'.format(city))

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    #Month to Start Time - New column called month
    df['month'] = df['Start Time'].dt.month

    #filter by month

    if month != 'all':
    
    # months to integer
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    # filtered month - New dataframe
        df = df[df['month'] == month]

    # Day from start Time - New column called month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by day
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    start_time = time.time()

    # Display the most common month AND NAME
    common_month = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print('most common month: %s ' % common_month)
    print('most common month name: %s ' %  months[common_month-1])

    # Display the most common day of week
    common_weekday = df['day_of_week'].mode()[0]
    print('most common day of the week: %s' % common_weekday)

    # Display the most common start hour
    common_start_hour =  df['Start Time'].dt.hour.mode()[0]
    print('most common start hour: %s' % common_start_hour)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('most common start station: %s' % common_start_station)

    # Display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('most common end station: %s' % common_end_station)

    # Display most frequent combination of start station and end station trip
    most_frequent_comb_start_station = (df['Start Station'] + df['End Station']).mode()[0]
    print('most frequent combination: %s' % most_frequent_comb_start_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time %s' % total_travel_time)

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time %s' % mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_counts = df['User Type'].value_counts()
    print(user_types_counts)


    # Display counts of gender
    if 'Gender' in df:
        gender_types_count = df['Gender'].value_counts()
        print(gender_types_count)
    else:
        print("no gender information in city")

    print()

    # Display earliest, most recent, and most common year of birth
    # Display counts of gender
    if 'Birth Year' in df:
        earliest_common_year = df['Birth Year'].min()
        print('earliest common year %s' % earliest_common_year)

        common_most_recent_year = df['Birth Year'].max()
        print('common most recent year %s' % common_most_recent_year)

        most_common_year = df['Birth Year'].mode()[0]
        print('most common year %s' % most_common_year)
    else:
        print("no birth year information in city")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#User choice - 5 lines of raw data or not

runs = 0
def raw_data(df):

    data = 0
    while (input('do you want to see raw data, yes or no: \n').lower() == 'yes' and (data+5)<len(df)):
            print(df[data:data+5])
            data += 5
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
