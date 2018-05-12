# Maze generate

* 创建一个Cell类，就是用来画在窗口上的单元。

  ```python
  class Cell():
      def __init__(self, x, y):
          global width
          self.x = x * width
          self.y = y * width
          
          self.visited = False
          self.current = False
          
          self.walls = [True, True, True, True] # top , right , bottom , left
          
          # neighbors
          self.neighbors = []
          
          self.top = 0
          self.right = 0
          self.bottom = 0
          self.left = 0
          
          self.next_cell = 0
      
      def draw(self):
          if self.current:
              pygame.draw.rect(screen, RED, (self.x, self.y, width, width))
          elif self.visited:
              pygame.draw.rect(screen, WHITE, (self.x, self.y, width, width))
          
              if self.walls[0]:
                  pygame.draw.line(screen, BLACK, (self.x, self.y), ((self.x + width), self.y), 1) # top
              if self.walls[1]:
                  pygame.draw.line(screen, BLACK, ((self.x + width), self.y), ((self.x + width), (self.y + width)), 1) # right
              if self.walls[2]:
                  pygame.draw.line(screen, BLACK, ((self.x + width), (self.y + width)), (self.x, (self.y + width)), 1) # bottom
              if self.walls[3]:
                  pygame.draw.line(screen, BLACK, (self.x, (self.y + width)), (self.x, self.y), 1) # left
      
      def check_neighbors(self):
          if int(self.y / width) - 1 >= 0:
              self.top = grid[int(self.y / width) - 1][int(self.x / width)]
          if int(self.x / width) + 1 <= cols - 1:
              self.right = grid[int(self.y / width)][int(self.x / width) + 1]
          if int(self.y / width) + 1 <= rows - 1:
              self.bottom = grid[int(self.y / width) + 1][int(self.x / width)]
          if int(self.x / width) - 1 >= 0:
              self.left = grid[int(self.y / width)][int(self.x / width) - 1]
          
          if self.top != 0:
              if self.top.visited == False:
                  self.neighbors.append(self.top)
          if self.right != 0:
              if self.right.visited == False:
                  self.neighbors.append(self.right)
          if self.bottom != 0:
              if self.bottom.visited == False:
                  self.neighbors.append(self.bottom)
          if self.left != 0:
              if self.left.visited == False:
                  self.neighbors.append(self.left)
          
          if len(self.neighbors) > 0:
              self.next_cell = self.neighbors[random.randrange(0, len(self.neighbors))]
              return self.next_cell
          else:
              return False

  ```

  类的成员包括坐标信息，墙信息，是否被访问过，是否是当前位置，周围cell信息。

  成员函数draw()用来绘制，主要调用pygame的draw函数。

  成员函数check_neighbor()用来随机查找周围的单元，从而随机生成迷宫。

* remove_walls函数，cell默认是有四面墙，该函数用于删除部分墙，生成迷宫。

  ```python
  def remove_walls(current_cell, next_cell):
      x = int(current_cell.x / width) - int(next_cell.x / width)
      y = int(current_cell.y / width) - int(next_cell.y / width)
      if x == -1: # right of current
          current_cell.walls[1] = False
          next_cell.walls[3] = False
      elif x == 1: # left of current
          current_cell.walls[3] = False
          next_cell.walls[1] = False
      elif y == -1: # bottom of current
          current_cell.walls[2] = False
          next_cell.walls[0] = False
      elif y == 1: # top of current
          current_cell.walls[0] = False
          next_cell.walls[2] = False
  ```

* init_grid函数，初始化迷宫

  ```python
  def init_grid(rows, cols):
      grid = []
      for y in range(rows):
          grid.append([])
          for x in range(cols):
              grid[y].append(Cell(x, y))

      return grid, grid[0][0], 0

  ```

* main工作流程

  ```python
      pygame.init()
      WHITE = (255,255,255)
      GREY = (20,20,20)
      BLACK = (0,0,0)
      PURPLE = (100,0,100)
      RED = (255,0,0)
      size = (701,701)
      screen = pygame.display.set_mode(size)
      pygame.display.set_caption("Maze Generator")
      done = False
      clock = pygame.time.Clock()
      width = 25
      cols = int(size[0] / width)
      rows = int(size[1] / width)
      stack = []
      grid = []

      grid, current_cell, next_cell = init_grid(rows, cols)

      while not done:
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  done = True
          
          screen.fill(GREY)
          
          current_cell.visited = True
          current_cell.current = True
          
          for y in range(rows):
              for x in range(cols):
                  grid[y][x].draw()
          
          next_cell = current_cell.check_neighbors()
          
          if next_cell != False:
              current_cell.neighbors = []
              
              stack.append(current_cell)
              
              remove_walls(current_cell, next_cell)
              
              current_cell.current = False
              
              current_cell = next_cell
          
          elif len(stack) > 0:
              current_cell.current = False
              current_cell = stack.pop()
              
          elif len(stack) == 0:
              grid, current_cell, next_cell = init_grid(rows, cols)
          
          pygame.display.flip()
          
          clock.tick(600)

      pygame.quit()

  ```

* 效果

  ![maze](./maze.gif)

