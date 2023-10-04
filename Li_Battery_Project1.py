import pybamm

models = [
    pybamm.lithium_ion.SPM(),
    pybamm.lithium_ion.SPMe(),
]

sims = []

for model in models:
    sim = pybamm.Simulation(model)
    sim.solve([0, 10])
    sims.append(sim)
    
pybamm.dynamic_plot(sims, time_unit = "hours")    