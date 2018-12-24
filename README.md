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