---
source: https://mauricioaniche.com/publications/testing-meets-code-review/
source_date: 2018
researched: 2026-09-26
---

# When Testing Meets Code Review: Why and How Developers Review Tests (Spadini et al., ICSE 2018)

Primary source: peer-reviewed empirical study. How it was read this time: the publication page (curl, abstract) and the full paper PDF from an archive.org copy of sback.it/publications/icse2018b.pdf via pdftotext, read for methods, results (RQ1 to RQ3) and conclusions. (The earlier note had only the abstract.)

- Data: Gerrit reviews of Eclipse, OpenStack and Qt, more than 300,000 reviews; manual classification of 600 review comments on test files; 12 interviews (3 with developers of the studied projects, 9 more from open source and industry).
- RQ1: in reviews containing both test and production files, 43% of production files but 29% of test files received a comment (71% of test files received none); the odds of a production file being commented are 1.90 times higher ("Test files are almost 2 times less likely to be discussed"). The difference in comment number and length is small. In reviews with only one file type, test files were slightly more discussed (odds 1.15).
- RQ2, comment content on test files: code improvement 35% (of which about 40% about testing practices, 14% about tested and untested paths, 6% about wrong assertions), understanding 32%, social 11%, defect 9%, knowledge transfer 4%. About half of the defect comments concern severe, high-level testing issues (43% severe, 41% less severe, 14% wrong assertion handling).
- RQ3 and interviews: some developers read tests first, most read production first; reviewers lack test-specific context and navigation between test and production files is a main obstacle; the reported main cause of less discussion of tests is that "reviewers see testing as a secondary task and they are not aware of the risk of poor testing or bad reviewing".
- "Secondary importance" is in the paper's abstract as background and in the conclusions as a reported cause; it is not an independent measurement.
- Predates agents; does not study weakened or deleted tests.
