import arbor
import numpy, pandas, seaborn # You may have to pip install these.
import sys
import platform

# The corresponding generic recipe version of `single_cell_model.py`.

# (1) Define a recipe for a single cell and set of probes upon it.

class single_recipe (arbor.recipe):
    def __init__(self, cell, probes):
        # The base C++ class constructor must be called first, to ensure that
        # all memory in the C++ class is initialized correctly.
        arbor.recipe.__init__(self)
        self.the_cell = cell
        self.the_probes = probes

    def num_cells(self):
        return 1

    def num_sources(self, gid):
        return 1

    def cell_kind(self, gid):
        return arbor.cell_kind.cable

    def cell_description(self, gid):
        return self.the_cell

    def get_probes(self, gid):
        return self.the_probes





# (2) Create a cell.
# Associate labels to tags
labels = arbor.label_dict()
labels['soma']    = '(tag 0)'
labels['axon']    = '(tag 1)'
labels['dend_2']  = '(tag 2)'
labels['neur_3']  = '(tag 3)'
labels['neur_4']  = '(tag 4)'

# Build a segment tree
tree = arbor.segment_tree()

# Soma (tag = 0) with diameter 4.20119 μm, modelled as cylinder of height 4.20119 µm and radius 2.100595 µm
# arbor.mpoint(x, y, z, radius)
s0_0 = tree.append(arbor.mnpos, arbor.mpoint(-0.9, -231.95, 6.85, 4.20119), arbor.mpoint(-0.9, -227.74881, 6.85, 4.20119), tag=0)

# describe Axon (tag=1) attached to soma
# naming of segments ax_y with a = axon, x = number of axon segment, y = neuroML segment ID
a0_7 = tree.append(s0_0,  arbor.mpoint(-9.000000e-01, -2.319500e+02, 6.850000e+00, 0.78102493 / 2), arbor.mpoint(-9.000000e-01, -2.331500e+02, 7.700000e+00, 0.78102493/2), tag=1)
a1_8 = tree.append(a0_7, arbor.mpoint(-9.000000e-01, -2.365500e+02, 1.020000e+01, 0.64031243 / 2), tag=1)
a2_9 = tree.append(a1_8, arbor.mpoint(-9.000000e-01, -2.425500e+02, 1.470000e+01, 0.5744563  / 2), tag=1)
a3_10 = tree.append(a2_9, arbor.mpoint(5.500000e-01, -2.436000e+02, 1.470000e+01, 0.5744563 / 2), tag=1)
a4_11 = tree.append(a3_10, arbor.mpoint(2.900000e+00, -2.436000e+02, 1.470000e+01, 0.56568545 / 2), tag=1)
a5_12 = tree.append(a4_11, arbor.mpoint(6.975000e+00, -2.435250e+02, 1.517500e+01, 0.622495 / 2), tag=1)
a6_13 = tree.append(a5_12, arbor.mpoint(1.420000e+01, -2.421500e+02, 1.920000e+01, 0.5744563 / 2), tag=1)
a7_14 = tree.append(a6_13, arbor.mpoint(1.792500e+01, -2.400500e+02, 2.560000e+01, 0.5408327 / 2), tag=1)
a8_15 = tree.append(a7_14, arbor.mpoint(1.950000e+01, -2.378000e+02, 3.232500e+01, 0.60207975 / 2), tag=1)
a9_16 = tree.append(a8_15, arbor.mpoint(1.792500e+01, -2.355500e+02, 3.907500e+01, 0.50497526 / 2), tag=1)
a10_17 = tree.append(a9_16, arbor.mpoint(1.420000e+01, -2.334500e+02, 4.550000e+01, 0.5744563 / 2), tag=1)
a11_18 = tree.append(a10_17, arbor.mpoint(6.975000e+00, -2.321000e+02, 4.952500e+01, 0.81547534 / 2), tag=1)
a12_19 = tree.append(a11_18, arbor.mpoint(2.900000e+00, -2.319500e+02, 4.990000e+01, 0.36055514 / 2), tag=1)
a13_20 = tree.append(a12_19, arbor.mpoint(-1.000000e-01, -2.322000e+02, 4.902500e+01, 0.42720017 / 2), tag=1)
a14_21 = tree.append(a12_19, arbor.mpoint(-5.000000e-01, -2.321750e+02, 4.900000e+01, 0.68007356 / 2), tag=1)

# describe dendrite_2 (tag 2) attached to the soma
# naming of segments dend2_x_y with dend2 = dendrite 2, x = number of dendrite segment, y = neuroML segment ID
dend2_0_1 = tree.append(s0_0, arbor.mpoint(-9.000000e-01, -2.319500e+02, 6.850000e+00, 0.64031243 / 2), arbor.mpoint(-9.000000e-01, -2.307500e+02, 6.000000e+00, 0.64031243 / 2), tag=2)
dend2_1_2 = tree.append(dend2_0_1, arbor.mpoint(-1.450000e+00, -2.265000e+02, 2.850000e+00, 0.46904156 / 2), tag=2)
dend2_2_3 = tree.append(dend2_1_2, arbor.mpoint(-1.450000e+00, -2.149500e+02, -5.250000e+00, 0.4358899 / 2), tag=2)
dend2_3_4 = tree.append(dend2_2_3, arbor.mpoint(-1.450000e+00, -2.102000e+02, -8.400000e+00, 0.5 / 2), tag=2)
dend2_4_5 = tree.append(dend2_3_4, arbor.mpoint(-1.450000e+00, -1.968000e+02, -1.760000e+01, 0.5 / 2), tag=2)
dend2_5_6 = tree.append(dend2_4_5, arbor.mpoint(-1.450000e+00, -1.947500e+02, -1.895000e+01, 0.4358899 / 2), tag=2)

# describe neurite_3 (tag 3) attached to axon
# naming of segments neur3_x_y with neur3 = neurite 3, x = number of neurite segment, y = neuroML segment ID
neur3_0_22 = tree.append(a14_21, arbor.mpoint(-5.000000e-01, -2.321750e+02, 4.900000e+01, 0.68007356 / 2), arbor.mpoint(-7.000000e-01, -2.325000e+02, 4.910000e+01, 0.56568545 / 2), tag=3)
neur3_1_23 = tree.append(neur3_0_22, arbor.mpoint(-7.000000e-01, -2.363500e+02, 5.060000e+01, 0.5744563 / 2), tag=3)
neur3_2_24 = tree.append(neur3_1_23, arbor.mpoint(-7.000000e-01, -2.377500e+02, 5.105000e+01, 0.6480741 / 2), tag=3)

# describe neurite_4 (tag 4) attached to axon
# naming of segments neur4_x_y with neur4 = neurite 4, x = number of neurite segment, y = neuroML segment ID
neur4_0_25 = tree.append(a14_21, arbor.mpoint(-5.000000e-01, -2.321750e+02, 4.900000e+01, 0.68007356 / 2), arbor.mpoint(-7.000000e-01, -2.318500e+02, 4.890000e+01, 0.5744563 / 2), tag=4)
neur4_1_26 = tree.append(neur4_0_25, arbor.mpoint(-7.000000e-01, -2.107500e+02, 4.070000e+01, 0.5744563 / 2), tag=4)
neur4_2_27 = tree.append(neur4_1_26, arbor.mpoint(-7.000000e-01, -2.059500e+02, 3.770000e+01, 0.5744563 / 2), tag=4)
neur4_3_28 = tree.append(neur4_2_27, arbor.mpoint(-7.000000e-01, -1.762500e+02, 1.840000e+01, 0.5744563 / 2), tag=4)
neur4_4_29 = tree.append(neur4_3_28, arbor.mpoint(-7.000000e-01, -1.740500e+02, 1.700000e+01, 0.5744563 / 2), tag=4)


# Mark location for synapse at the midpoint of branch 1 (first dendrite)
#labels['synapse_site'] = '(location 1 0.5)'

# Mark the root of the tree.
labels['root'] = '(root)'

# create dd1 morphology
morph = arbor.morphology(tree)

# create cell
dd1_cell = arbor.cable_cell(morph, labels)

# neuroML: <specificCapacitance value="1 uF_per_cm2"/>, <initMembPotential value="-45 mV"/>, <resistivity value="12 kohm_cm"/>
# set cable properties
# Vm = initial membrane potential (-45 mV)
# cm = membrane capacitance (0.01 F / m²)
# rL = axial resistivity of cable (12000 Ohm * cm)
# tempK = temperature in Kelvin (not provided by c302)
dd1_cell.set_properties(Vm = -45, cm = 0.01, rL = 12000)

#cat = arbor.default_catalogue()

# define dynamics / mechanisms
# neuroML: <channelDensity id="Leak_all" ionChannel="Leak" condDensity="0.02 mS_per_cm2" erev="-50 mV" ion="non_specific"/>
#leak_all = arbor.mechanism("pas/e=-50/g=2e-05")
Leak = arbor.mechanism("Leak")


# neuroML: <channelDensity id="k_slow_all" ionChannel="k_slow" condDensity="2 mS_per_cm2" erev="-60 mV" ion="k"/>
# dd1_cell.set_ion("k", int_con = 140, ext_con = 5, method = arbor.mechanism('nernst/x=k'))
# k_slow_all = arbor.mechanism("k_slow_all", {"g": 2e-03, "e": -60})
k_slow = arbor.mechanism("k_slow")


# neuroML: <channelDensity id="k_fast_all" ionChannel="k_fast" condDensity="0.2 mS_per_cm2" erev="-60 mV" ion="k"/>
# k_fast_all = arbor.mechanism("k_fast_all", {"g": 2e-04, "e": -60})
k_fast = arbor.mechanism("k_fast")

# neuroML: <species id="ca" concentrationModel="CaPool" ion="ca" initialConcentration="0 mM" initialExtConcentration="2E-6 mol_per_cm3"/>
#dd1_cell.set_ion("ca", int_con=0, ext_con=2, method=arbor.mechanism('nernst/x=ca'))
CaPoolTH = arbor.mechanism("CaPoolTH")


# neuroML: <channelDensity id="ca_boyle_all" ionChannel="ca_boyle" condDensity="2 mS_per_cm2" erev="40 mV" ion="ca"/>
ca_boyle_all = arbor.mechanism("ca_boyle")

# put hh dynamics on soma and passive properties on the dendrites
dd1_cell.paint('"soma"', 'Leak')
dd1_cell.paint('"soma"', 'k_slow')
dd1_cell.paint('"soma"', 'k_fast')
dd1_cell.paint('"soma"', 'CaPoolTH')
dd1_cell.paint('"soma"', 'ca_boyle')

#cell.paint('"dend"', 'pas')

# Attach a single synapse.
#cell.place('"synapse_site"', 'expsyn')

# define location at centre of soma
labels['soma_centre'] = '(location 0 0.5)'


# place current stimulus on soma centre
# interface arbor.iclamp(start_time [ms], duration [ms], offset_current [nA])

dd1_cell.place('(location 0 0.5)', arbor.iclamp(100, 300, 0.0087)) # 8.7 pA == 0.0087 nA

# neuroML: <spikeThresh value="-26 mV"/>
# Attach a spike detector with threshold of -26 mV
dd1_cell.place('(location 0 0.5)', arbor.spike_detector(-26))


#print(platform.python_version())


#cat = arbor.default_catalogue()
#print(cat.has("Leak"))
#print(cat.keys())






# (3) Instantiate recipe with a voltage probe.

recipe = single_recipe(dd1_cell, [arbor.cable_probe_membrane_voltage('(location 0 0.5)')])
#arbor.cable_probe('voltage', arbor.location(0, 0.5))

# (4) Instantiate simulation and set up sampling on probe id (0, 0).
context = arbor.context()
domains = arbor.partition_load_balance(recipe, context)
sim = arbor.simulation(recipe, domains, context)

sim.record(arbor.spike_recording.all)
handle = sim.sample((0, 0), arbor.regular_schedule(0.1))

# (6) Run simulation for 30 ms of simulated activity and collect results.

sim.run(tfinal=500)
spikes = sim.spikes()
data, meta = sim.samples(handle)[0]

# (7) Print spike times, if any.

if len(spikes)>0:
    print('{} spikes:'.format(len(spikes)))
    for t in spikes['time']:
        print('{:3.3f}'.format(t))
else:
    print('no spikes')

# (8) Plot the recorded voltages over time.

print("Plotting results ...")
seaborn.set_theme() # Apply some styling to the plot
df = pandas.DataFrame({'t/ms': data[:, 0], 'U/mV': data[:, 1]})
seaborn.relplot(data=df, kind="line", x="t/ms", y="U/mV", ci=None).savefig('single_cell_recipe_result.svg')

# (9) Optionally, you can store your results for later processing.

df.to_csv('single_cell_recipe_result.csv', float_format='%g')

