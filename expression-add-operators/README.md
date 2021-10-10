<h2>282. Expression Add Operators</h2><h3>Hard</h3><hr><div><p>Given a string <code>num</code> that contains only digits and an integer <code>target</code>, return <em><strong>all possibilities</strong> to insert the binary operators </em><code>'+'</code><em>, </em><code>'-'</code><em>, and/or </em><code>'*'</code><em> between the digits of </em><code>num</code><em> so that the resultant expression evaluates to the </em><code>target</code><em> value</em>.</p>

<p>Note that operands in the returned expressions <strong>should not</strong> contain leading zeros.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> num = "123", target = 6
<strong>Output:</strong> ["1*2*3","1+2+3"]
<strong>Explanation:</strong> Both "1*2*3" and "1+2+3" evaluate to 6.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> num = "232", target = 8
<strong>Output:</strong> ["2*3+2","2+3*2"]
<strong>Explanation:</strong> Both "2*3+2" and "2+3*2" evaluate to 8.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> num = "105", target = 5
<strong>Output:</strong> ["1*0+5","10-5"]
<strong>Explanation:</strong> Both "1*0+5" and "10-5" evaluate to 5.
Note that "1-05" is not a valid expression because the 5 has a leading zero.
</pre>

<p><strong>Example 4:</strong></p>

<pre><strong>Input:</strong> num = "00", target = 0
<strong>Output:</strong> ["0*0","0+0","0-0"]
<strong>Explanation:</strong> "0*0", "0+0", and "0-0" all evaluate to 0.
Note that "00" is not a valid expression because the 0 has a leading zero.
</pre>

<p><strong>Example 5:</strong></p>

<pre><strong>Input:</strong> num = "3456237490", target = 9191
<strong>Output:</strong> []
<strong>Explanation:</strong> There are no expressions that can be created from "3456237490" to evaluate to 9191.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num.length &lt;= 10</code></li>
	<li><code>num</code> consists of only digits.</li>
	<li><code>-2<sup>31</sup> &lt;= target &lt;= 2<sup>31</sup> - 1</code></li>
</ul>
</div>