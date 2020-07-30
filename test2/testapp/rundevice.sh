for i in `adb devices | grep 'device$' | awk '{print $1}'`
do
  echo $i
  udid=$i pytest /Users/zhangtao/PycharmProjects/pyzt1/test2/testapp/test_search.py &
done