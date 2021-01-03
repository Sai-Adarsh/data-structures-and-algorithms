<h2>526. Beautiful Arrangement</h2><h3>Medium</h3><hr><div><p>Suppose you have <code>n</code> integers from <code>1</code> to <code>n</code>. We define a beautiful arrangement as an array that is constructed by these <code>n</code> numbers successfully if one of the following is true for the <code>i<sup>th</sup></code> position (<code>1 &lt;= i &lt;= n</code>) in this array:</p>

<ul>
	<li>The number at the <code>i<sup>th</sup></code> position is divisible by <code>i</code>.</li>
	<li><code>i</code> is divisible by the number at the <code>i<sup>th</sup></code> position.</li>
</ul>

<p>Given an integer <code>n</code>, return <em>the number of the beautiful arrangements that you can construct</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> 2
<b>Explanation:</b> 
The first beautiful arrangement is [1, 2]:
Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
The second beautiful arrangement is [2, 1]:
Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 15</code></li>
</ul>
</div>