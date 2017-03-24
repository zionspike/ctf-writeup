# JVM - 25
```
Attachment: rev25.zip
```
```
[+] extract rev25.zip
rev25.zip:
	- EKO.class
```
There is a file named EKO.class. I open it with JD-Gui.jar and I found couple lines of Java code.
```java
public class EKO
{
  public static void main(String[] paramArrayOfString)
  {
    int i = 0;
    for (int j = 0; j < 1337; j++) {
      i += j;
    }
    String str = "EKO{" + i + "}";
  }
}
```

Here I just print the variable **str** and got the flag
```java
public class EKO
{
  public static void main(String[] paramArrayOfString)
  {
    int i = 0;
    for (int j = 0; j < 1337; j++) {
      i += j;
    }
    String str = "EKO{" + i + "}";
    System.out.print(str);
  }
}
```

Then I've got flag.
* EKO{893116}
