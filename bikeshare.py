import time
import pandas as pd

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
    city = input('Would you like to see data for Chicago, New York, or Washington? ').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('Invalid input. Please try again. ').lower()

    # Ask if they want to filter by month, day, or not at all?
    filter = input('Would you like to filter the data by month, day, both, or not at all?' ).lower()

    if filter == 'month':
    # TO DO: get user input for month (all, january, february, ... , june)
        day = 'all'
        month = input('Which month - January, February, March, April, May, or June? ').lower()
        while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            month = input('Invalid input. Please try again. ').lower()

    if filter == 'day':
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        month = 'all'
        day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ').lower()
        while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            day = input('Invalid input. Please try again. ').lower()

    if filter == 'both':
        month = input('Which month - January, February, March, April, May, or June? ').lower()
        while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            month = input('Invalid input. Please try again. ').lower()

        day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ').lower()
        while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            day = input('Invalid input. Please try again. ').lower()

    else:
        month = 'all'
        day = 'all'

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

    # Load file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time into new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filter by month
    if month != 'all':
        # Use the index of the months list to get the corresponding integer
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filter by month to create new dataframe
        df = df[df['month'] == month]

    # Filter by day of week
    if day != 'all':
        # Filter by the day of week to create new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # Find mode of column
    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)

    # TO DO: display the most common day of week
    # Find mode of column
    common_day = df['day_of_week'].mode()[0]
    print('Most Common Day of the Week:', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    # Find mode of column
    common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    # Combine the start and end station into one string
    df['combo'] = df['Start Station'] + ' ' + '/' + ' ' + df['End Station']
    # Create dictionary counter using for loop
    combo_counter = {}
    for trip in df['combo']:
        if trip not in combo_counter:
            combo_counter[trip] = 1
        else: combo_counter[trip] += 1
    # Sort list of dictionary's keys
    sorted_combo = sorted(combo_counter.keys())
    # Find element with highest count
    most_freq_combo = sorted_combo[-1]
    print('Most frequent combination of start station and end station trip:', most_freq_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types: \n', user_types)

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    print('Counts of gender: \n', gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    # Find earliest year of birth
    earliest_year = df['Birth Year'].min()
    print('Earliest year of birth: ', int(earliest_year))
    # Find most recent year of birth
    recent_year = df['Birth Year'].max()
    print('Most recent year of birth: ', int(recent_year))
    # Find most common year of birth
    common_year = df['Birth Year'].mode()
    print('Most common year of birth: ', int(common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Prompt user if they would like to view raw data
        index = 0
        view_raw_data = input('\n Would you like to view raw trip data? Enter yes or no. \n').lower()
        while True:
            if view_raw_data == 'yes':
                print(df.iloc[index:index+5])
                index += 5
                view_raw_data = input('\n Would you like to view additional data? Enter yes or no. \n').lower()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
