//
//  Section.h
//  Qcumber
//
//  Created by Chris Cooper on 11-10-19.
//  Copyright (c) 2011 Chris Cooper. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <CoreData/CoreData.h>

@class Course, SectionComponent, SectionType, Term;

@interface Section : NSManagedObject {
@private
}
@property (nonatomic, retain) NSString * id;
@property (nonatomic, retain) NSString * index;
@property (nonatomic, retain) NSSet *components;
@property (nonatomic, retain) Course *course;
@property (nonatomic, retain) Term *term;
@property (nonatomic, retain) SectionType *type;
@end

@interface Section (CoreDataGeneratedAccessors)

- (void)addComponentsObject:(SectionComponent *)value;
- (void)removeComponentsObject:(SectionComponent *)value;
- (void)addComponents:(NSSet *)values;
- (void)removeComponents:(NSSet *)values;
@end
