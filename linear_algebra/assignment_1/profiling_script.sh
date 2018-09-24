#!/bin/bash
for i in {3..99}
do
    cmnd="python second_problem_using_numpy.py input_files/profile_input_second_random$i"
    cmnd_user="python second_problem.py input_files/profile_input_second_random$i"
    result=$($cmnd)
    result_user=$($cmnd_user)
    echo "$i & $result & $result_user \\\\"
done
