# nueral-mmo
Multi-Agent RL implementations for the Neural MMO’s procedurally generated environments.

### Compitition Setting

1. Team of 8 agents (therefore 8 obs and actions), against 15 other teams (total of 16 teams competting) on a 128-x-128 map.
2. 1024 Time Steps 
3. Four main categories of tasks: Foraging, Combat, Equipment and Exploration. 
4. Hetrogenous Agents


### Observation Space 

Observation dict: A Total of 128 individual agents 

`observation[agent_id=1]` = Entity and Title
1. Entity : personal infor, other platesr and npcs
2. Tile: Local map information. 

