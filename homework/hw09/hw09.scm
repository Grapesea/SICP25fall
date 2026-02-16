;;; Homework 09: Macro

; ANSWER QUESTION wwsd

;;; Required Problems

(define (find n lst)
  'YOUR-CODE-HERE
)


(define (find-nest n sym)
  'YOUR-CODE-HERE
)


(define-macro (my/or operands)
  'YOUR-CODE-HERE
)


(define-macro (k-curry fn args vals indices)
  ''YOUR-CODE-HERE
)


(define-macro (let* bindings expr)
  ''YOUR-CODE-HERE
)

;;; Just For Fun Problems


; Helper Functions for you
(define (cadr lst) (car (cdr lst)))
(define (cddr lst) (cdr (cdr lst)))
(define (caddr lst) (car (cdr (cdr lst))))
(define (cdddr lst) (cdr (cdr (cdr lst))))

(define-macro (infix expr)
  'YOUR-CODE-HERE
)


; only testing if your code could expand to a valid expression 
; resulting in my/and/2 and my/or/2 not hygienic
(define (gen-sym) 'sdaf-123jasf/a123)

; in these two functions you can use gen-sym function.
; assumption:
; 1. scm> (eq? (gen-sym) (gen-sym))
;    #f
; 2. all symbol generate by (gen-sym) will not in the source code before macro expansion
(define-macro (my/and/2 operands)
  'YOUR-CODE-HERE
)

(define-macro (my/or/2 operands)
  'YOUR-CODE-HERE
)
