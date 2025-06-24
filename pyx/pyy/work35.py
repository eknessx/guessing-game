#this code will sort about the team skills and hired users and de

#importing data classes
from dataclasses import dataclass
from typing import List

#Team class and sorting the members skills
@dataclass
class TeamMember:
    name: str
    position: str
    salary: int
    skills: List[str]
    experience: int

#team member skills
team = [
    TeamMember("Lysara", "artist", 35000, ["painting", "3D modeling"], 5),
    TeamMember("Ekness", "developer", 36000, ["python", "c#", "unity"], 4),
    TeamMember("GlueSquare", "writer", 30000, ["writing", "music composer","game designer"], 4),
]

#function to determine the team cases
def sortCases():
    #Team requirements
    req_arist={"painting","3D modeling"}
    req_coder={"unity","c#"}
    req_writer={"game designer","music composer"}

    #The values will remain false if there no artist
    has_artist=False
    has_coder=False
    has_writer=False

    #loops throught the condintion at least not best way and like wtf 
    #i found the issubset function by coincidence like python has to mutch functions wtf
    for person in team:
        skills=set(person.skills)
        if req_arist.issubset(skills):
            print(f"{person.name} matches all required skills.")
            has_artist=True
        elif req_coder.issubset(skills):
            print(f"{person.name} matches all required skills.")
            has_coder=True
        elif req_writer.issubset(skills):
            print(f"{person.name} matches all required skills.")
            has_writer=True
        elif has_artist and has_coder and has_writer:
            print("Team is capable of making a project!")
            return True
sortCases()
