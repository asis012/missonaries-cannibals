import math
import pydot

graph= pydot.Dot(graph_type='digraph')
#______________________________________________________________________________
# Missionaries and Cannibals Problem

class State():
	def __init__(self, cannibalLeft, missionaryLeft, boat, cannibalRight, missionaryRight, game):
		self.cannibalLeft = cannibalLeft
		self.missionaryLeft = missionaryLeft
		self.boat = boat
		self.cannibalRight = cannibalRight
		self.missionaryRight = missionaryRight
		self.parent = None
		self.game=game

	def is_goal(self):
		if self.cannibalLeft == 0 and self.missionaryLeft == 0:
			return True
		else:
			return False

	def is_valid(self):
		if self.missionaryLeft >= 0 and self.missionaryRight >= 0 \
				   and self.cannibalLeft >= 0 and self.cannibalRight >= 0 \
				   and (self.missionaryLeft == 0 or self.missionaryLeft >= self.cannibalLeft) \
				   and (self.missionaryRight == 0 or self.missionaryRight >= self.cannibalRight):
			return True
		else:
			return False


	def __eq__(self, other):
		return self.cannibalLeft == other.cannibalLeft and self.missionaryLeft == other.missionaryLeft \
				   and self.boat == other.boat and self.cannibalRight == other.cannibalRight \
				   and self.missionaryRight == other.missionaryRight \
				   and self.game==other.game



	def __hash__(self):
		return hash((self.cannibalLeft, self.missionaryLeft, self.boat, self.cannibalRight, self.missionaryRight, self.game))

def successors(cur_state):
	children = [];
	if cur_state.boat == 'left':
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft - 2, 'right',
								  cur_state.cannibalRight, cur_state.missionaryRight + 2, cur_state.game)
		## Two missionaries cross left to right.

		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
			new_state.game=None

		else:
			new_state.game="over"
			new_state=cur_state
			children.append(new_state)


		new_state = State(cur_state.cannibalLeft - 2, cur_state.missionaryLeft, 'right',
								  cur_state.cannibalRight + 2, cur_state.missionaryRight, cur_state.game)
		## Two cannibals cross left to right.

		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
			new_state.game= None

		else:
			cur_state.game="over"
			new_state=cur_state
			children.append(new_state)


		new_state = State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft - 1, 'right',
								  cur_state.cannibalRight + 1, cur_state.missionaryRight + 1, cur_state.game)
		## One missionary and one cannibal cross left to right.

		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
			new_state.game=None

		else:
			cur_state.game="over"
			new_state=cur_state
			children.append(new_state)


		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft - 1, 'right',
								  cur_state.cannibalRight, cur_state.missionaryRight + 1, cur_state.game)
		## One missionary crosses left to right.

		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
			new_state.game=None

		else:
			new_state.game="over"
			new_state=cur_state
			children.append(new_state)


		new_state = State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft, 'right',
								  cur_state.cannibalRight + 1, cur_state.missionaryRight, cur_state.game)
		## One cannibal crosses left to right.

		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
			new_state.game=None

		else:
			new_state.game="over"
			new_state=cur_state
			children.append(new_state)

	else:
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft + 2, 'left',
								  cur_state.cannibalRight, cur_state.missionaryRight - 2, cur_state.game)
		## Two missionaries cross right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
			new_state.game=None

		else:
			new_state.game="over"
			new_state=cur_state
			children.append(new_state)


		new_state = State(cur_state.cannibalLeft + 2, cur_state.missionaryLeft, 'left',
								  cur_state.cannibalRight - 2, cur_state.missionaryRight, cur_state.game)
		## Two cannibals cross right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
			new_state.game=None

		else:
			new_state.game="over"
			new_state=cur_state
			children.append(new_state)


		new_state = State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft + 1, 'left',
								  cur_state.cannibalRight - 1, cur_state.missionaryRight - 1, cur_state.game)
		## One missionary and one cannibal cross right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
			new_state.game=None

		else:
			new_state.game="over"
			new_state=cur_state
			children.append(new_state)


		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft + 1, 'left',
								  cur_state.cannibalRight, cur_state.missionaryRight - 1, cur_state.game)
		## One missionary crosses right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
			new_state.game=None

		else:
			new_state.game="over"
			new_state=cur_state
			children.append(new_state)


		new_state = State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft, 'left',
								  cur_state.cannibalRight - 1, cur_state.missionaryRight, cur_state.game)
		## One cannibal crosses right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
			new_state.game=None

		else:
			new_state.game="over"
			new_state=cur_state
			children.append(new_state)



	return children




def breadth_first_search():
	initial_state = State(3,3,'left',0,0, None)
	if initial_state.is_goal():
		return initial_state
	frontier = list()
	explored = set()
	frontier.append(initial_state)

	while frontier:
		state = frontier.pop(0)
		if state.is_goal():
			node=pydot.Node("[%s,%s,%s]"%(str(state.cannibalLeft),str(state.missionaryLeft),state.boat),style='filled',fillcolor='blue')
			graph.add_node(node)
			return state
		explored.add(state)
		children = successors(state)

		#l= children[0].__dict__
		#print(l)
		for child in children:
			if (child not in explored) or (child not in frontier):
				frontier.append(child)
				allnode_list=list()


	return none

def print_solution(solution):
		path = []
		path.append(solution)
		parent = solution.parent
		node_list=list()
		notokaynode_list= list()
		while parent:
			path.append(parent)
			parent = parent.parent

		for t in range(len(path)):
			state = path[len(path) - t - 1]

			node_okay=pydot.Node("[%s,%s,%s]"%(str(state.cannibalLeft),str(state.missionaryLeft),state.boat),style='filled',color='green')
			graph.add_node(node_okay)
			node_list.append(node_okay)



			print ("(" + str(state.cannibalLeft) + "," + str(state.missionaryLeft) \
							  + "," + state.boat + "," + str(state.cannibalRight) + "," + \
							  str(state.missionaryRight) + ")"+ str(state.game))
		#1st level other nodes
		node_32=pydot.Node("[%d,%d,%s]"%(3,2,'right'),style='filled',fillcolor='red')
		node_22=pydot.Node("[%d,%d,%s]"%(2,2,'right'),style='filled',fillcolor='red')
		node_23=pydot.Node("[%d,%d,%s]"%(2,3,'right'),style='filled',fillcolor='red')
		node_31=pydot.Node("[%d,%d,%s]"%(3,1,'right'),style='filled',fillcolor='red')
		#2nd level other nodes
		node_32l=pydot.Node("[%d,%d,%s]"%(3,2,'left'),style='filled',fillcolor='red')
		#3rd level other nodes
		node_21=pydot.Node("[%d,%d,%s]"%(2,1,'right'),style='filled',fillcolor='red')
		node_12=pydot.Node("[%d,%d,%s]"%(1,2,'right'),style='filled',fillcolor='red')
		#4th level other nodes
		node_02=pydot.Node("[%d,%d,%s]"%(0,2,'right'),style='filled',fillcolor='red')
		#5th level other nodes
		node_21l=pydot.Node("[%d,%d,%s]"%(2,1,'left'),style='filled',fillcolor='red')
		node_31l=pydot.Node("[%d,%d,%s]"%(3,1,'left'),style='filled',fillcolor='red')
		node_12l=pydot.Node("[%d,%d,%s]"%(1,2,'left'),style='filled',fillcolor='red')

		notokaynode_list.extend((node_32,node_22,node_23,node_31,node_32l,node_21,node_12,node_02,node_21l,node_31l,node_12l))
		graph.add_node(node_32)
		graph.add_node(node_22)
		graph.add_node(node_23)
		graph.add_node(node_31)
		graph.add_node(node_32l)
		graph.add_node(node_21)
		graph.add_node(node_12)
		graph.add_node(node_02)
		graph.add_node(node_21l)
		graph.add_node(node_31l)
		graph.add_node(node_12l)
		#Adding edges 1st level
		for t in range(0,4):
			edge_notokay=pydot.Edge(node_list[0],notokaynode_list[t])
			graph.add_edge(edge_notokay)

		#Adding edges 2nd level
		for t in range(4,5):
			edge_notokay=pydot.Edge(node_22,notokaynode_list[t])
			graph.add_edge(edge_notokay)

		#Adding edges in 3rd level
		for t in range(5,7):
			edge_notokay=pydot.Edge(node_list[2],notokaynode_list[t])
			graph.add_edge(edge_notokay)

		#Adding edges in 4th level
		for t in range(7,8):
			edge_notokay=pydot.Edge(node_list[4],notokaynode_list[t])
			graph.add_edge(edge_notokay)
		#Adding edges in 5th level
		for t in range(8,11):
			edge_notokay=pydot.Edge(node_list[5],notokaynode_list[t])
			graph.add_edge(edge_notokay)
		for l in range(len(path)-1):

			edge_okay=pydot.Edge(node_list[l],node_list[l+1])
			graph.add_edge(edge_okay)


		#Invisible nodes for texts
		legendnode=pydot.Node("Index",shape='none',fontcolor='teal',fontsize='35')
		graph.add_node(legendnode)
		graph.add_edge(pydot.Edge(node_31,legendnode,style='invis'))
		#bodypart
		#bodynode=pydot.Node("asjdhdjasjdajksdhajsdhkjashda",shape='box',fontcolor='white',fontsize='10')
		#graph.add_node(bodynode)
		#graph.add_edge(pydot.Edge(legendnode,bodynode,style='invis'))
		#greeen node
		greennode=pydot.Node(". ",style='filled',fillcolor='green',fontcolor='green')
		graph.add_node(greennode)
		graph.add_edge(pydot.Edge(legendnode,greennode,style='invis'))
		#red
		rednode=pydot.Node(" ",style='filled',fillcolor='red')
		graph.add_node(rednode)
		graph.add_edge(pydot.Edge(greennode,rednode,style='invis'))


		#Solution node
		solunode=pydot.Node("Solution node",shape='none',fontcolor='blue')
		graph.add_node(solunode)
		graph.add_edge(pydot.Edge(legendnode,solunode,style='invis'))


		#Killed Node
		killednode=pydot.Node("Killed Node",shape='none',fontcolor='blue')
		graph.add_node(killednode)
		graph.add_edge(pydot.Edge(solunode,killednode,style='invis'))

		#Goal Node
		goalnode=pydot.Node("Goal Node",shape='none',fontcolor='blue')
		graph.add_node(goalnode)
		graph.add_edge(pydot.Edge(killednode,goalnode,style='invis'))

		#Blue
		bluenode=pydot.Node(".",style='filled',fillcolor='blue')
		graph.add_node(bluenode)
		graph.add_edge(pydot.Edge(rednode,bluenode,style='invis'))

		#descript node
		descnode= pydot.Node("Node[x,y,z]=> x,y= Number of Cannibal and Missionary on the left bank",shape='none',fontcolor='blue')
		graph.add_node(descnode)
		zdesc=pydot.Node("z=> position of the boat",shape='none',fontcolor='blue')
		graph.add_node(zdesc)
		graph.add_edge(pydot.Edge(goalnode,descnode,style='invis'))
		graph.add_edge(pydot.Edge(descnode,zdesc,style='invis'))


		#footernode
		footernode= pydot.Node("Missionary And Cannibal Problem Solution State",shape='none',fontsize='50',fontcolor='orange')
		graph.add_node(footernode)
		graph.add_edge(pydot.Edge(footernode,node_list[11],style='invis'))


def main():
	solution = breadth_first_search()
	print ("Missionaries and Cannibals solution:")
	print ("(cannibalLeft,missionaryLeft,boat,cannibalRight,missionaryRight)")
	print_solution(solution)
#writing in filled
	graph.write_png('mercenarycannspacetree.png')


main()
