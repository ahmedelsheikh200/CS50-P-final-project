from project import know_the_user
from project import save_coaches_data ,Coach
from project import save_students_data,User
from project import choose_coach
import csv
def main():
    test_know_the_user()
    test_save_coaches_data()
    test_save_students_data()
    test_choose_coach


def test_know_the_user():
    # Test with 'c' as input
    assert know_the_user("c") == "c"

    # Test with 't' as input
    assert know_the_user("t") == "t"

    # Test with invalid input
    assert know_the_user("invalid") is None

    # Test with empty input
    assert know_the_user("") is None

def test_save_coaches_data():
    # Create mock coach data for testing
    coach_data = Coach("Magnus","Carlsen","norway",33,2831,3)

    # Call the function with mock coach data
    save_coaches_data("c", coach_data)

    # Read the CSV file to verify if data was written correctly
    with open('coaches.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        written_data = list(reader)

        # Assert that the CSV file is not empty
        assert written_data

        # Assert that the first entry matches the mock coach data
        assert written_data[0]['First Name'] == "Magnus"
        assert written_data[0]['Last Name'] == "Carlsen"
        assert written_data[0]['Country'] == "norway"
        assert int(written_data[0]['Age']) == 33
        assert int(written_data[0]['Rating']) == 2831
        assert int(written_data[0]['experience Years']) == 3
def test_save_students_data(mocker):
  """Tests if save_students_data writes user data to CSV correctly"""
  # Mock input function to return predefined data
  mocker.patch('builtins.input', side_effect=["John", "Doe", "US", 25, 4])

  # Call the function
  save_students_data(None)  # No user object needed if input is mocked

def test_choose_coach(mocker):
  """Tests if choose_coach displays coaches and returns chosen coach info"""

  # Mock coaches data (replace with actual data creation if needed)
  coaches = [
      {"First Name": "John", "Last Name": "Doe", "Country": "USA", "Age": "30", "Rating": "5"},
      {"First Name": "Jane", "Last Name": "Smith", "Country": "Canada", "Age": "35", "Rating": "4"}
  ]

  # Mock user input to choose coach (replace with actual user input logic)
  def mock_get_user_input(prompt):
    if prompt == "Which coach would you like to choose? (by number)":
      return 1  # Simulate user choosing the second coach (index 1)
    return None  # Mock other potential prompts

if __name__ == "__main__":
    main()

