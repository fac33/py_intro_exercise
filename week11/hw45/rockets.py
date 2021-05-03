################################################################################
# Author:Fanyang Cheng
# Date: 04/12/2021
# Description: This program gives two classes of rockets (common one and reusable
# one) and calculate for the total cost for each launch.
################################################################################
#define class rocket and reusable rockets.
class Rocket:
    def __init__(self,name,booster_cost,upper_stage_cost,fuel_cost):
        self.booster_cost = booster_cost
        self.upper_stage_cost = upper_stage_cost
        self.fuel_cost = fuel_cost
        self.name = name
    def cost_per_launch(self):
        tc = self.booster_cost+self.upper_stage_cost+self.fuel_cost
        print('This ',self.name,' cost $',format(tc,'.2f'),' million per launch.',sep = '')

class ReusableRocket(Rocket):
    def __init__(self,name,booster_cost,upper_stage_cost,fuel_cost,uses):
        super().__init__(name,booster_cost,upper_stage_cost,fuel_cost)
        self.uses = uses
    def cost_per_launch(self):
        tc = self.booster_cost/self.uses+self.upper_stage_cost+self.fuel_cost
        print('This ',self.name,' cost $',format(tc,'.2f'),' million per launch.',sep = '')
def main():
    #build each rockets' dataset
    atlasv = Rocket('Atlas V',65.4,42.6,0.23)
    aria = Rocket('Ariane 5',83.5,55.6,0.69)
    longm = Rocket('Long March 3B',28.5,19.0,2.38)
    soyu = Rocket('Soyuz 2',20.9,13.9,0.24)
    falc = ReusableRocket('Falcon 9',43.0,18.6,0.45,10)
    #print the answer.
    atlasv.cost_per_launch()
    aria.cost_per_launch()
    longm.cost_per_launch()
    soyu.cost_per_launch()
    falc.cost_per_launch()


if __name__ == '__main__':
    main()
