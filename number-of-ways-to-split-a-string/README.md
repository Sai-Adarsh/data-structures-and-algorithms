<h2>1573. Number of Ways to Split a String</h2><h3>Medium</h3><hr><div><p>Given a binary string <code>s</code> (a string consisting only of '0's and '1's),&nbsp;we can split <code>s</code>&nbsp;into 3 <strong>non-empty</strong> strings s1, s2, s3 (s1+ s2+ s3 = s).</p>

<p>Return the number of ways <code>s</code> can be split such that the number of&nbsp;characters '1' is the same in s1, s2, and s3.</p>

<p>Since the answer&nbsp;may be too large,&nbsp;return it modulo&nbsp;10^9 + 7.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "10101"
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are four ways to split s in 3 parts where each part contain the same number of letters '1'.
"1|010|1"
"1|01|01"
"10|10|1"
"10|1|01"
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "1001"
<strong>Output:</strong> 0
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "0000"
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are three ways to split s in 3 parts.
"0|0|00"
"0|00|0"
"00|0|0"
</pre>

<p><strong>Example 4:</strong></p>

<pre><strong>Input:</strong> s = "100100010100110"
<strong>Output:</strong> 12
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= s.length &lt;= 10^5</code></li>
	<li><code>s[i]</code> is <code>'0'</code>&nbsp;or&nbsp;<code>'1'</code>.</li>
</ul>
</div>