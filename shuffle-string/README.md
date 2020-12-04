<h2>unknown-problem</h2><h3>Easy</h3><hr><div><p>Given a string <code>s</code>&nbsp;and an integer array <code>indices</code> of the <strong>same length</strong>.</p>

<p>The string <code>s</code> will be shuffled such that the character at the <code>i<sup>th</sup></code> position moves to&nbsp;<code>indices[i]</code> in the shuffled string.</p>

<p>Return <em>the shuffled string</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/07/09/q1.jpg" style="width: 321px; height: 243px;">
<pre><strong>Input:</strong> s = "codeleet", <code>indices</code> = [4,5,6,7,0,2,1,3]
<strong>Output:</strong> "leetcode"
<strong>Explanation:</strong> As shown, "codeleet" becomes "leetcode" after shuffling.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "abc", <code>indices</code> = [0,1,2]
<strong>Output:</strong> "abc"
<strong>Explanation:</strong> After shuffling, each character remains in its position.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "aiohn", <code>indices</code> = [3,1,4,2,0]
<strong>Output:</strong> "nihao"
</pre>

<p><strong>Example 4:</strong></p>

<pre><strong>Input:</strong> s = "aaiougrt", <code>indices</code> = [4,0,2,6,7,3,1,5]
<strong>Output:</strong> "arigatou"
</pre>

<p><strong>Example 5:</strong></p>

<pre><strong>Input:</strong> s = "art", <code>indices</code> = [1,0,2]
<strong>Output:</strong> "rat"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>s.length == indices.length == n</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>s</code> contains only lower-case English letters.</li>
	<li><code>0 &lt;= indices[i] &lt;&nbsp;n</code></li>
	<li>All values of <code>indices</code> are unique (i.e. <code>indices</code> is a permutation of the integers from <code>0</code> to <code>n - 1</code>).</li>
</ul></div>