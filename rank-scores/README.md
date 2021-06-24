<h2>178. Rank Scores</h2><h3>Medium</h3><hr><div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg></a></div><div><p>Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.</p>

<pre>+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
</pre>

<p>For example, given the above <code>Scores</code> table, your query should generate the following report (order by highest score):</p>

<pre>+-------+---------+
| score | Rank    |
+-------+---------+
| 4.00  | 1       |
| 4.00  | 1       |
| 3.85  | 2       |
|&nbsp;3.65  | 3       |
| 3.65  | 3       |
| 3.50  | 4       |
+-------+---------+
</pre>

<p><strong>Important Note:</strong>&nbsp;For MySQL solutions, to escape reserved words used as column names, you can use an apostrophe before and after the keyword. For example<strong>&nbsp;`Rank`</strong>.</p>
</div>