for i in `adb devices | grep 'device$' | awk '{print $1}'`
do
  echo $i
  udid=$i pytest /Users/zhangtao/PycharmProjects/pyzt1/appium0102/appium01/testcase/test_add.py &
done