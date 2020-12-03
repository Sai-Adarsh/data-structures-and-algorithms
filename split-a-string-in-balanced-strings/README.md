<h2>1221. Split a String in Balanced Strings</h2><h3>Easy</h3><hr><div><p><i data-stringify-type="italic">Balanced</i>&nbsp;strings are those who have equal quantity of 'L' and 'R' characters.</p>

<p>Given a balanced string&nbsp;<code data-stringify-type="code">s</code>&nbsp;split it in the maximum amount of balanced strings.</p>

<p>Return the maximum amount of splitted balanced strings.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "RLRRLLRLRL"
<strong>Output:</strong> 4
<strong>Explanation: </strong>s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "RLLLLRRRLR"
<strong>Output:</strong> 3
<strong>Explanation: </strong>s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "LLLLRRRR"
<strong>Output:</strong> 1
<strong>Explanation: </strong>s can be split into "LLLLRRRR".
</pre>

<p><strong>Example 4:</strong></p>

<pre><strong>Input:</strong> s = "RLRRRLLRLL"
<strong>Output:</strong> 2
<strong>Explanation: </strong>s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i] = 'L' or 'R'</code></li>
</ul>
</div>