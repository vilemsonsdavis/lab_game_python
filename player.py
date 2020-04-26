import pygame

kin1_fr1 = pygame.image.load('lab_game/kin1_fr1.gif')
kin1_fr2 = pygame.image.load('lab_game/kin1_fr2.gif')
kin1_bk1 = pygame.image.load('lab_game/kin1_bk1.gif')
kin1_bk2 = pygame.image.load('lab_game/kin1_bk2.gif')
kin1_lf1 = pygame.image.load('lab_game/kin1_lf1.gif')
kin1_lf2 = pygame.image.load('lab_game/kin1_lf2.gif')
kin1_rt1 = pygame.image.load('lab_game/kin1_rt1.gif')
kin1_rt2 = pygame.image.load('lab_game/kin1_rt2.gif')
skl1_fr1 = pygame.image.load('lab_game/skl1_fr1.gif')
skl1_fr2 = pygame.image.load('lab_game/skl1_fr2.gif')
skl1_bk1 = pygame.image.load('lab_game/skl1_bk1.gif')
skl1_bk2 = pygame.image.load('lab_game/skl1_bk2.gif')
skl1_lf1 = pygame.image.load('lab_game/skl1_lf1.gif')
skl1_lf2 = pygame.image.load('lab_game/skl1_lf2.gif')
skl1_rt1 = pygame.image.load('lab_game/skl1_rt1.gif')
skl1_rt2 = pygame.image.load('lab_game/skl1_rt2.gif')
chr1_fr1 = pygame.image.load('lab_game/chr1_fr1.gif')
chr1_fr2 = pygame.image.load('lab_game/chr1_fr2.gif')
chr1_bk1 = pygame.image.load('lab_game/chr1_bk1.gif')
chr1_bk2 = pygame.image.load('lab_game/chr1_bk2.gif')
chr1_lf1 = pygame.image.load('lab_game/chr1_lf1.gif')
chr1_lf2 = pygame.image.load('lab_game/chr1_lf2.gif')
chr1_rt1 = pygame.image.load('lab_game/chr1_rt1.gif')
chr1_rt2 = pygame.image.load('lab_game/chr1_rt2.gif')
wmg2_fr1 = pygame.image.load('lab_game/wmg2_fr1.gif')
wmg2_fr2 = pygame.image.load('lab_game/wmg2_fr2.gif')
wmg2_bk1 = pygame.image.load('lab_game/wmg2_bk1.gif')
wmg2_bk2 = pygame.image.load('lab_game/wmg2_bk2.gif')
wmg2_lf1 = pygame.image.load('lab_game/wmg2_lf1.gif')
wmg2_lf2 = pygame.image.load('lab_game/wmg2_lf2.gif')
wmg2_rt1 = pygame.image.load('lab_game/wmg2_rt1.gif')
wmg2_rt2 = pygame.image.load('lab_game/wmg2_rt2.gif')

king = [kin1_fr1, kin1_fr2, kin1_bk1, kin1_bk2, kin1_lf1, kin1_lf2, kin1_rt1, kin1_rt2]
skeleton = [skl1_fr1, skl1_fr2, skl1_bk1, skl1_bk2, skl1_lf1, skl1_lf2, skl1_rt1, skl1_rt2]
predator = [chr1_fr1, chr1_fr2, chr1_bk1, chr1_bk2, chr1_lf1, chr1_lf2, chr1_rt1, chr1_rt2]
grandpa = [wmg2_fr1, wmg2_fr2, wmg2_bk1, wmg2_bk2, wmg2_lf1, wmg2_lf2, wmg2_rt1, wmg2_rt2]

class Player(object):
    def __init__(self, player_name, lab_game, walls):
        self.x = 1
        self.y = 51
        self.player_name = player_name
        self.lab_game = lab_game
        self.walls = walls
        self.player_pics = self.playerl = self.playerr = self.playerd = self.playeru = []
        self.pic = None
        self.check_player()
        self.walk_count = 0

    def check_player(self):
        if self.player_name == 'king':
            self.player_pics = king
        if self.player_name == 'predator':
            self.player_pics = predator
        if self.player_name == 'skeleton':
            self.player_pics = skeleton
        if self.player_name == 'grandpa':
            self.player_pics = grandpa

        self.pic = self.player_pics[0]

        self.playerl = [self.player_pics[4], self.player_pics[5]]
        self.playerr = [self.player_pics[6], self.player_pics[7]]
        self.playeru = [self.player_pics[2], self.player_pics[3]]
        self.playerd = [self.player_pics[0], self.player_pics[1]]

    def draw_player(self):
        self.lab_game.blit(self.pic, (self.x, self.y))

    def move_player(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if self.x > 1:
                self.x -= 1
            self.pic = self.playerl[int((self.walk_count % 40) / 20)]
            self.walk_count += 1
        if keys[pygame.K_RIGHT]:
            if self.x < 981:
                self.x += 1
            self.pic = self.playerr[int((self.walk_count % 40) / 20)]
            self.walk_count += 1
        if keys[pygame.K_UP]:
            if self.y > 51:
                self.y -= 1
            self.pic = self.playeru[int((self.walk_count % 40) / 20)]
            self.walk_count += 1
        if keys[pygame.K_DOWN]:
            if self.y < 631:
                self.y += 1
            self.pic = self.playerd[int((self.walk_count % 40) / 20)]
            self.walk_count += 1

        self.check_wall()

    def check_if_possible_to_walk(self, wall_one, wall_two, wall_three, direction):
        if wall_one not in self.walls or wall_two not in self.walls or \
                ((wall_one != wall_two and wall_one in self.walls and wall_two in self.walls) \
                 and wall_three not in self.walls):
            if direction == 'right':
                self.x -= 1
            elif direction == 'left':
                self.x += 1
            elif direction == 'up':
                self.y += 1
            elif direction == 'down':
                self.y -= 1

    def check_wall(self):
        if (self.x + 18) % 20 == 0: #right side wall
            wall_one_y = self.y - ((self.y-10)%20) + 1
            wall_two_y = (self.y + 18) - ((self.y+8)%20) + 1
            wall_x = self.x + 18

            wall_one = ((wall_x, wall_one_y), (wall_x, wall_one_y + 18 ))
            wall_two = ((wall_x, wall_two_y), (wall_x, wall_two_y + 18 ))
            wall_three = ((self.x+19, wall_one_y + 19), (self.x+37, wall_one_y + 19))

            self.check_if_possible_to_walk(wall_one, wall_two, wall_three, 'right')

        if self.x % 20 == 0: #left side wall
            wall_one_y = self.y - ((self.y-10)%20) + 1
            wall_two_y = (self.y + 18) - ((self.y+8)%20) + 1
            wall_x = self.x

            wall_one = ((wall_x, wall_one_y), (wall_x, wall_one_y + 18 ))
            wall_two = ((wall_x, wall_two_y), (wall_x, wall_two_y + 18 ))
            wall_three = ((self.x-19, wall_one_y + 19), (self.x-1, wall_one_y + 19))

            self.check_if_possible_to_walk(wall_one, wall_two, wall_three, 'left')

        if self.y % 20 == 10: #above side wall
            wall_one_x = self.x - (self.x%20) + 1
            wall_two_x = (self.x + 18) - ((self.x+18)%20) + 1
            wall_y = self.y

            wall_one = ((wall_one_x, wall_y), (wall_one_x + 18, wall_y ))
            wall_two = ((wall_two_x, wall_y), (wall_two_x + 18, wall_y ))
            wall_three = ((wall_one_x + 19, self.y-19), (wall_one_x + 19, self.y-1))

            self.check_if_possible_to_walk(wall_one, wall_two, wall_three, 'up')

        if (self.y + 18) % 20 == 10: #below side wall
            wall_one_x = self.x - (self.x % 20) + 1
            wall_two_x = (self.x + 18) - ((self.x + 18) % 20) + 1
            wall_y = self.y + 18

            wall_one = ((wall_one_x, wall_y), (wall_one_x + 18, wall_y))
            wall_two = ((wall_two_x, wall_y), (wall_two_x + 18, wall_y))
            wall_three = ((wall_one_x + 19, self.y + 19), (wall_one_x + 19, self.y + 37))

            self.check_if_possible_to_walk(wall_one, wall_two, wall_three, 'down')



