# Name:        Saffa Gbondo
# Name:        Marima Andrew Mambondiumwe - Navigator
# Name:        Kyaw Hpone Myint - Driver
# Purpose:     Backtracking and Caves
# Created:     10/30/2016
# Acknowledgement:  We worked on the codes and lab writeups together; so, they are essentially the same.
#                   But we submitted individually on the moodle.
#Acknowledgemnt:    concept for read_map function is obtained from CSC 226 assignment A14 Caesar Cipher
#                   Source code of Stack.py is provided by Dr. Jan
#-------------------------------------------------------------------------------

from Stack import Stack
import copy
import sys

class Crawler:
    '''
    This is a class definition for Crawler, which contains the class methods to move, keep track of treasures, all the junctions, and all the branches in the map.
    '''

    def __init__(self, myPosition, my_map):
        '''
        Constructor definition initializing all the values. myPosition is the array containing coordinates for current position of the treasure hunter.
        '''
        self.pos = myPosition
        self.treasure_count = 0 # this will keep track of the number of  treasures found
        self.cur_map = my_map
        self.steps_count = 0
        self.branches = Stack()
        self.prev_steps = Stack()
        self.branch_pt = Stack()
        self.convert_map_to_text(self.cur_map)

    def inc_treasure(self):
        '''Increments the amount of treasure by one'''
        self.treasure_count += 1
        print('Total amounts of treasures: ' + str(self.treasure_count))

    def move_crawler(self, position_to_move):
        '''Find the direction available for the crawler to move. Moves the crawler one position in the direction found. '''
        #update the current position according the inputs
        temp = copy.deepcopy(self.pos)
        self.pos[0] = position_to_move[0]
        self.pos[1] = position_to_move[1]
        #increment the number of step and update the map after each step
        self.increase_step()
        self.Update_map(temp)

    def increase_step(self):
        '''track the number of move'''
        self.steps_count += 1

    def convert_map_to_text(self, mapList):
        '''Convert the 2D map array into a string for printing'''
        map = ""
        for pos in mapList:
            map = map + ''.join(pos) + '\n'
        print map

    def Update_map(self, old_position):
        '''update the current position of the map after moving'''
        self.cur_map[old_position[0]][old_position[1]] = '*' # This will put a '*' in the positions already traversed by the crawler
        self.cur_map[self.pos[0]][self.pos[1]] = 'M' # set the current position as 'M'
        text = self.convert_map_to_text(self.cur_map)

    def check_location(self):
        '''track what is around the current position and move to one of the position in the following order west>east>north>south'''

        #these array keep track of the north, west, east and south position from a current point
        mov_north = [0,0]
        mov_west = [0,0]
        mov_east = [0,0]
        mov_south = [0,0]

        #moving in 4 different direction by changing index values of the current position
        mov_north[0] = self.pos[0]-1
        mov_north[1] = self.pos[1]

        mov_west[0] = self.pos[0]
        mov_west[1] = self.pos[1]-1

        mov_east[0] = self.pos[0]
        mov_east[1] = self.pos[1]+1

        mov_south[0] = self.pos[0]+1
        mov_south[1] = self.pos[1]

        #get the item at the specified location in the map to check later on (item can be W, ., T or *)
        at_north = self.cur_map[mov_north[0]][mov_north[1]]
        at_west = self.cur_map[mov_west[0]][mov_west[1]]
        at_east = self.cur_map[mov_east[0]][mov_east[1]]
        at_south = self.cur_map[mov_south[0]][mov_south[1]]

        path_list = [] # Will contain the words to return indicating the possible directions to go to

        #check whether there is a treasure in all four directions, and append it to the path_list to use later on
        if at_west == "T":
            path_list.append(mov_west)
        if at_east == "T":
            path_list.append(mov_east)
        if at_north == "T":
            path_list.append(mov_north)
        if at_south == "T":
            path_list.append(mov_south)


        path_list = self.remov_used_pos(path_list)

        # if there are multiple path available, then the junction point is recorded to come back later
        if len(path_list) > 1:
            self.update_step_branches()

        # checks whether we are at the end of the path or not; if not, we will add the current postion to the most recent branch, and keep moving in the chosen path
        if len(path_list) > 0:
            self.inc_cur_branch()
            self.move_crawler(path_list[0])
            self.prev_steps.push(self.pos)
            self.inc_treasure()
            return

        # check whether there is a path in all four directions, and append it to the path_list to use later on
        if at_west == '.':
            path_list.append(mov_west)
        if at_east == '.':
            path_list.append(mov_east)
        if at_north == '.':
            path_list.append(mov_north)
        if at_south == '.' :
            path_list.append(mov_south)
        path_list = self.remov_used_pos(path_list)


        if len(path_list) > 1:# this point is recorded so that the explorer can come back later
            self.update_step_branches()

        if len(path_list) > 0:# the explorer will move to the first in option in path_list
            print('')
            print('')
            cur_step = copy.deepcopy(self.pos)
            self.inc_cur_branch()
            self.move_crawler(path_list[0])
            self.prev_steps.push(cur_step)
            return
        else:
            self.back_to_last_junction()


    def remov_used_pos(self, position_list):
        '''
            Checks whether current position coordinate in the path list are already used up or not in a given branch
        '''
        for item in position_list:
            # this will remove the traversed position from our path list
            if item in self.prev_steps.items:
                position_list.remove(item)
        return position_list


    def back_to_last_junction(self):
        '''
        Put the treasure hunter back to the last junction points. The treasure hunter will back track his steps back toward the last junction point using the data structure that we stored earlier.
        '''

        if self.branch_pt.size() <= 0:
            print('Treasures found: ' + str(self.treasure_count))
            sys.exit()

        # this will make sure the treasure hunter has reached all the points before he/she reaches the end of the path
        else:
            cur_step = copy.deepcopy(self.pos)
            sub_branch = self.branches.pop()
            for i in range(sub_branch.size()):
                x = sub_branch.pop()
                self.move_crawler(x)
            self.branch_pt.pop()
            self.prev_steps.push(cur_step)


    def inc_cur_branch(self):
        '''
        Check whether the branch is empty or not. If empty, we will create a sub branch with current position coordinate.
        If not, we will add the current position coordinate to the already existing sub branch
        '''
        temp_pos = copy.deepcopy(self.pos)
        if self.branches.size() > 0:
            self.branches.items[-1].push(temp_pos)
        else:
            stack = Stack()
            self.branches.push(stack)
            self.branches.items[-1].push(temp_pos)

    def update_step_branches(self):
        '''
        keep track of the current position of the treasure hunter and will keep track of the steps before the next function call.
        If there were steps recorded before this, they will be deleted
        '''

        cur_branch = Stack()
        self.branch_pt.push(self.pos)
        self.branches.push(cur_branch)





