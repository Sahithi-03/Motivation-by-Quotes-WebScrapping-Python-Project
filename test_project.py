#Necessary libraries
import project                         #The actual python file
from unittest.mock import patch        #To mimic the random module

#Test for inspiration() function
@patch('project.scrapping_website', return_value='\n“To the well-organized mind, death is but the next great adventure.”\n- by J.K. Rowling\n')
def test_inspiration(mocked_scrapping_website):
    result = project.inspiration()
    assert result == '\n“To the well-organized mind, death is but the next great adventure.”\n- by J.K. Rowling\n'

#Test for love() function
@patch('project.scrapping_website', return_value='\n"It is better to be hated for what you are than to be loved for what you are not.”\n- by André Gide\n')
def test_love(mocked_scrapping_website):
    r=project.love()
    assert r == '\n"It is better to be hated for what you are than to be loved for what you are not.”\n- by André Gide\n'

#Test for life() function
@patch('project.scrapping_website', return_value='\n“Good friends, good books, and a sleepy conscience: this is the ideal life.”\n- by Mark Twain\n')
def test_life(mocked_scrapping_website):
    res=project.life()
    assert res == '\n“Good friends, good books, and a sleepy conscience: this is the ideal life.”\n- by Mark Twain\n'

