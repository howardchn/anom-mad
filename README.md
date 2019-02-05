# Compare Anomoly Detection with Percentile and MAD

## Precondition to run sample
Enter python virtual environment and install dependencies.
```
$ source bin/activate
$ pip install -r requirements.txt
```

## Percentile
Just make sure the points are plot in 95% area in the graph. Try sample with:

```
$ python main.py -a percentile
```

![screenshot-percentile](https://github.com/howardchn/anom-mad/raw/master/images/anom-percentile.png)

## MAD (Median absolute deviation)
Use MAD to detect the anomaly points. Try sample with:

```
$ python main.py
```

![screenshot-mad](https://github.com/howardchn/anom-mad/raw/master/images/anom-mad.png)

-- Update Feb 3, 2019 --
With MAD, we could find the outerliner and render it out.
```
$ python main.py -a mad_flow
```

![screenshot-mad-flow](https://github.com/howardchn/anom-mad/raw/master/images/anom-mad-flow.png)

Also with Percentile, the outerline is rendered as:
```
$ python main.py -a percentile_flow
```

![screenshot-percentile_flow](https://github.com/howardchn/anom-mad/raw/master/images/anom-percentile-flow.png)