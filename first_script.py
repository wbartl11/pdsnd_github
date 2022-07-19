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
    city = ''
    while city not in CITY_DATA.keys():
            city = input('Would you like to see data for Chicago, New York City, or Washington?:').lower()
            if city not in CITY_DATA.keys():

                print('That\'s not a valid input! Please try again')


    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = ''
    while  month not in month_list:
        month = input('If you would like to filter by month, please enter a month from January to June. If not, please enter \'all\':').lower()

        if month not in month_list:
            print('That\'s not a valid input! Please try again')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    day = ''
    while day not in day_list:
        day = input('If you would like to filter by day, please enter the day of the week. If not, please enter \'all\':').lower()

        if day not in day_list:
            print('That\'s not a valid input! Please try again')

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
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

    month_dict = {1 : 'January', 2 : 'February', 3 : 'March', 4 : 'April', 5 : 'May', 6 : 'June'}
    popular_month = df['month'].mode()[0]
    print('The most popular month is: {}'.format(month_dict[popular_month]))

    popular_day = df['day_of_week'].mode()[0]
    print('The most popular day of the week is: {}'.format(popular_day))
    # TO DO: display the most common day of week

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common hour is:', popular_hour)
    # TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    comm_startstation = df['Start Station'].mode()[0]
    count_comm_startstation = df['Start Station'].value_counts()[comm_startstation]
    print('The most common start station was: {}, people started here {} times'.format(comm_startstation, count_comm_startstation))

    comm_endstation = df['End Station'].mode()[0]
    count_comm_endstation = df['End Station'].value_counts()[comm_endstation]
    print('The most common end station was: {}, people ended here {} times'.format(comm_endstation, count_comm_endstation))

    df['Trip'] = df['Start Station'] + " to " + df['End Station']
    comm_trip = df['Trip'].mode()[0]
    count_comm_trip = df['Trip'].value_counts()[comm_trip]

    print('The most common trip was: {}, it occurred {} times'.format(comm_trip, count_comm_trip))


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    total_travel_time_prop = divmod(total_travel_time, 3600)

    total_travel_time_prop2 = divmod(total_travel_time_prop[1], 60)

    print('The total travel was {} hours and {} minute(s).'.format(int(total_travel_time_prop[0]), int(total_travel_time_prop2[0])))

    avg_travel_time = df['Trip Duration'].mean()

    avg_travel_time_prop = divmod(avg_travel_time, 60)


    print("The average time was {} minutes and {} second(s)".format(int(avg_travel_time_prop[0]), int(avg_travel_time_prop[1])))

    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_type = df['User Type']
        count_user_type = user_type.value_counts(dropna=True)
        print("The amount of users by type can be seen below: \n" + str(count_user_type))
    except:
        print('no user type')

    # TO DO: Display counts of gender
    try:
        df_gender = df['Gender']
        gender_count = df_gender.value_counts(dropna=True)
        print("\nThe types of users by gender are seen below:\n\n{}".format(gender_count))
    except:
        print("No gender data provided")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        birth_year = df['Birth Year']
        comm_birth_year = birth_year.mode()[0]
        print('The most common year of birth was:', int(comm_birth_year))
    except:
        print('No birth year data provided')

    try:
        birth_year_early = int(df['Birth Year'].min())
        birth_year_late = int(df['Birth Year'].max())
        print("The earliest year of birth:\n {} \n\n The latest year of birth:\n {}".format(birth_year_early, birth_year_late))
    except:
        print("No birth year data provided")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    from tabulate import tabulate
    while True:
        see_raw_data = input('\nWould you like to see the next five row of raw data? Enter yes or no.\n')
        if see_raw_data.lower() != 'yes':
            break
        print(tabulate(df.iloc[np.arange(0+i,5+i)], headers = 'keys'))
        i+=5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
