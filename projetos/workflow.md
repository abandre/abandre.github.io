---
layout: page
title: Workflow Verification
---


**FORMAL WORKFLOW VERIFICATION WITH SPIN**
<br>Amaury B. Andre

<table width="100%">
	<tr><td align="center">
		<a href="http://www2.sbc.org.br/ce-webmedia/webmedia2009/index.php.103.html" target="_blank"><img src="webmedia.png"></a>
	</td><td>
		<br>III Workshop on Business Process Management 
		<br>Technical Session I - Service Oriented Architectures Arquitetura Orientada a Serviços & Services Composition
		<br>Monday, 05/10/2009 - Room Florença II -  14:40 às 16:20h
		<br><a href="http://www2.sbc.org.br/ce-webmedia/webmedia2009/index.php.103.html" target="_blank">Webmedia 2009</a>
	</td></tr>
</table>

<hr style="height:1px;border-width:0;color:gray;background-color:gray">

## Master's Dissertation

- **Institution:**	Universidade Estadual de Campinas (UNICAMP). Instituto de Computação
- **Defense date:**	2010
- **Examining board members:** Lucinéia Heloisa Thom; Arnaldo Vieira Moura
- **Advisor:**	Jacques Wainer
- **Sponsor:** FAPESP - Fundação de Amparo à Pesquisa do Estado de São Paulo (Processo #2007/57995-3)
- **Link:** [https://bv.fapesp.br/en/publicacao/75243/formal-workflow-verification-with-spin/](https://bv.fapesp.br/en/publicacao/75243/formal-workflow-verification-with-spin/)

### Abstract

Workflow management is a reality nowadays, but today's systems give very little support to verify correctness in workflow models. This work aims to perform formal verification, with the goal of detecting syntactic errors, like the existence of activities poorly modeled, in other words, activities with no precondition or effect. It is a goal too, the definition of workflows structural verification, as to detect if the process does not have deadlocks (state in which the process is stuck with no possibility of getting any further), or verifying if there are dead activities in the process (activities impossible to be reached), or if exist incomplete terminations, ie, pending transitions after the process reached its objectives. Besides syntactic and structural verifications, it is necessary too, to perform semantic verifications in the process, in other words, it is important to validate the processes in respect to characteristics of its logical organization, in a higher level of information than simply structural verification. For example, it is directly impacting in the quality of the process model the definition if it has resource access conflicts. In this way, a process that is structurally correct, can be stuck in a deadlock, due to the concurrency in the access of a common resource of distinct activities. Besides that, verifications of costs restrictions, for example, can spoil a process. All these verifications are important to decide if a workflow model is correct. The main contribution of this work is the definition of workflow processes modeling that makes it possible to perform syntactic, structural and semantic verifications, all in a unique tool, that is showed to be scalable for real process, and even possible to verify ad-hoc questions, specific to the model, as checking activities ordering, for example (AU)

[Back](../projetos)