<h2>916. Word Subsets</h2><h3>Medium</h3><hr><div><p>We are given two arrays <code>words1</code> and <code>words2</code> of words.&nbsp; Each word is a string of lowercase letters.</p>

<p>Now, say that&nbsp;word <code>b</code> is a subset of word <code>a</code><strong>&nbsp;</strong>if every letter in <code>b</code> occurs in <code>a</code>, <strong>including multiplicity</strong>.&nbsp; For example, <code>"wrr"</code> is a subset of <code>"warrior"</code>, but is not a subset of <code>"world"</code>.</p>

<p>Now say a word <code>a</code> from <code>words1</code> is <em>universal</em> if for every <code>b</code> in <code>words2</code>, <code>b</code>&nbsp;is a subset of <code>a</code>.&nbsp;</p>

<p>Return a list of all universal words in <code>words1</code>.&nbsp; You can return the words in any order.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre><strong>Input: </strong>words1 = <span id="example-input-1-1">["amazon","apple","facebook","google","leetcode"]</span>, words2 = <span id="example-input-1-2">["e","o"]</span>
<strong>Output: </strong><span id="example-output-1">["facebook","google","leetcode"]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre><strong>Input: </strong>words1 = <span id="example-input-2-1">["amazon","apple","facebook","google","leetcode"]</span>, words2 = <span id="example-input-2-2">["l","e"]</span>
<strong>Output: </strong><span id="example-output-2">["apple","google","leetcode"]</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre><strong>Input: </strong>words1 = <span id="example-input-3-1">["amazon","apple","facebook","google","leetcode"]</span>, words2 = <span id="example-input-3-2">["e","oo"]</span>
<strong>Output: </strong><span id="example-output-3">["facebook","google"]</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre><strong>Input: </strong>words1 = <span id="example-input-4-1">["amazon","apple","facebook","google","leetcode"]</span>, words2 = <span id="example-input-4-2">["lo","eo"]</span>
<strong>Output: </strong><span id="example-output-4">["google","leetcode"]</span>
</pre>

<div>
<p><strong>Example 5:</strong></p>

<pre><strong>Input: </strong>words1 = <span id="example-input-5-1">["amazon","apple","facebook","google","leetcode"]</span>, words2 = <span id="example-input-5-2">["ec","oc","ceo"]</span>
<strong>Output: </strong><span id="example-output-5">["facebook","leetcode"]</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= words1.length, words2.length &lt;= 10000</code></li>
	<li><code>1 &lt;= words1[i].length, words2[i].length&nbsp;&lt;= 10</code></li>
	<li><code>words1[i]</code> and <code>words2[i]</code> consist only of lowercase letters.</li>
	<li>All words in <code>words1[i]</code> are unique: there isn't <code>i != j</code> with <code>words1[i] == words1[j]</code>.</li>
</ol>
</div>
</div>
</div>
</div>
</div>
</div>