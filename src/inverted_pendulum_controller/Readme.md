### Dependencies
- [`simple-pid`](https://pypi.org/project/simple-pid/)

```bash
pip install simple-pid
```

### Setting up Environment 
- Open termainal in the directory.
- Type the following command: "source devel/setup.bash"

### Goal-1

- Type the following command: 
```bash
roslaunch inverted_pendulum_controller task1.launch"
```

### Goal-2
- Type the following command:
```bash
 "roslaunch inverted_pendulum_controller task2.launch"

```

### Goal-3

- Type the following command: 
```bash
"roslaunch inverted_pendulum_controller task3.launch"
```


### Note
- Graphs are plotted in rqt_plot.
- It may possible that graph is not scaled properly thus it won't make any sense.
- If so, Scale the rqt_plot graph properly for better understanding.
- The System works fine when the angle is in between(3.0 and 3.3).

