#!/bin/bash

# curlem.bash

# This script should use curl to run some simple tests.

curl localhost:5011/algo_demos
curl localhost:5011"/sklinear/FB/3/2017-08/'pct_lag1,slope3,dow,moy'",
curl localhost:5011"/sklinear_yr/FB/2/2017/'pct_lag1,slope3,dow,moy'",
curl localhost:5011"/sklinear_tkr/F/'pct_lag1,slope3,dow,moy'",
curl localhost:5011"/keraslinear/FB/3/2017-08/'pct_lag2,slope5,moy'",
curl localhost:5011"/keraslinear_yr/FB/2/2016/'pct_lag1,slope3,dow,moy'",
curl localhost:5011"/keraslinear_tkr/FB/2/'pct_lag1,slope3,dow,moy'",
curl localhost:5011"/keras_nn/FB/3/2017-07?features='pct_lag1,slope4,moy'&hl=2&neurons=4",
curl localhost:5011"/keras_nn_yr/FB/2/2017?features='pct_lag1,slope4,moy'&hl=2&neurons=4",
curl localhost:5011"/keras_nn_tkr/FB/2?features='pct_lag1,slope4,moy'&hl=2&neurons=4"

exit
