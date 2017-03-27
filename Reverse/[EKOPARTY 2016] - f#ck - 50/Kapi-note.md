# f#ck - 50
```
Attachment: rev50.zip
```
```
[+] extract rev50.zip
rev50.zip:
	- FlagGenerator.exe
```
```
root@AIRBUS:# file FlagGenerator.exe 
FlagGenerator.exe: PE32 executable (console) Intel 80386 Mono/.Net assembly, for MS Windows
```
There is a .Net binary and it like other .Net binary it could be decompiled. I decompile it with [ILSpy](http://ilspy.net/)

```java
public static class Program
{
  [Serializable]
  internal class teArr@9 : FSharpFunc<int, string>
  {
    public string str;

    public int[] ccIndices;

    internal teArr@9(string str, int[] ccIndices)
    {
      this.str = str;
      this.ccIndices = ccIndices;
    }

    public override string Invoke(int i)
    {
      if (i == this.ccIndices.Length - 1)
      {
        return this.str.Substring(i);
      }
      int num = this.ccIndices[i];
      return this.str.Substring(num, this.ccIndices[i + 1] - num);
    }
  }

  public static string get_flag(string str)
  {
    int[] array = StringInfo.ParseCombiningCharacters(str);
    int num = array.Length;
    FSharpFunc<int, string> fSharpFunc = new Program.teArr@9(str, array);
    if (num < 0)
    {
      Operators.Raise<Unit>(new ArgumentException(LanguagePrimitives.ErrorStrings.get_InputMustBeNonNegativeString(), "count"));
    }
    string[] array2 = new string[num];
    int num2 = 0;
    int num3 = num - 1;
    if (num3 >= num2)
    {
      do
      {
        array2[num2] = fSharpFunc.Invoke(num2);
        num2++;
      }
      while (num2 != num3 + 1);
    }
    string[] array3 = array2;
    Array.Reverse(array3);
    return string.Join("", array3);
  }

  [EntryPoint]
  public static int main(string[] argv)
  {
    if (argv.Length != 1)
    {
      ExtraTopLevelOperators.PrintFormatLine<Unit>(new PrintfFormat<Unit, TextWriter, Unit, Unit, Unit>("Usage: FlagGenerator.exe <FLAG>"));
    }
    else
    {
      string text = Program.get_flag("t#hs_siht_kc#f");
      if (string.Equals(text, argv[0]))
      {
        FSharpFunc<string, Unit> fSharpFunc = ExtraTopLevelOperators.PrintFormatLine<FSharpFunc<string, Unit>>(new PrintfFormat<FSharpFunc<string, Unit>, TextWriter, Unit, Unit, string>("EKO{%s}"));
        string text2 = text;
        fSharpFunc.Invoke(text2);
      }
      else
      {
        ExtraTopLevelOperators.PrintFormatLine<Unit>(new PrintfFormat<Unit, TextWriter, Unit, Unit, Unit>("BAD ANSWER"));
      }
    }
    return 0;
  }
}
```

Then I got the flag.
* EKO{f#ck_this_sh#t}
